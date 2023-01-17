
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from apps.profiles.serializers import ProfileSerializer
from apps.profiles.models import Profile
from apps.products.models import Product
from apps.products.serializers import ProducteSerializer

from apps.users.models import User


# main route all methods
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def product_list(request):
    # get all or by id route
    if request.method == "GET":
        products = Product.objects.all().order_by('-id')
        serializer = ProducteSerializer(products, many=True)
        return Response(serializer.data)
            
    # post method - no need in Products - user ref creates Products
    elif request.method == "POST":
        serializer = ProducteSerializer(data=request.data, context={'user': request.user})
        # print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',"DELETE","PUT"])
@permission_classes([IsAuthenticated])
def product_detail(request,pk):
    # get Product by id
    if request.method == "GET":
        try:
            products = Product.objects.get(id=pk)
            serializer = ProducteSerializer(products, many=False)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    # update Product by id
    elif request.method == "PUT":
        try:
            print(request.data)
            print(pk)
            product = Product.objects.get(id=pk)
            serializer = ProducteSerializer(instance=product, data=request.data, context={'user': request.user})
            if serializer.is_valid():
                print("yes")
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # delete Product by id
    elif request.method == "DELETE":
        try:
            product = Product.objects.get(id=pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except :
                return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
