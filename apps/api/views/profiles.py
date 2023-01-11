
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from apps.profiles.serializers import ProfileSerializer
from apps.profiles.models import Profile
from apps.users.models import User


# main route all methods
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_list(request):
    # get all or by id route
    if request.method == "GET":
        profiles = Profile.objects.all().order_by('-id')
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
            
    # # post method - no need in profiles - user ref creates profiles
    # elif request.method == "POST":
    #     serializer = ProfileSerializer(data=request.data)
    #     print(request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',"DELETE","PUT"])
@permission_classes([IsAuthenticated])
def profile_detail(request,pk):
    if request.method == "GET":
        try:
            profiles = Profile.objects.get(id=pk)
            serializer = ProfileSerializer(profiles, many=False)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    # update obj by id
    elif request.method == "PUT":
        try:
            profile = Profile.objects.get(id=pk)
            serializer = ProfileSerializer(instance=profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # delede obj by id
    elif request.method == "DELETE":
        try:
            profile = Profile.objects.get(id=pk)
            profile.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except :
                return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
