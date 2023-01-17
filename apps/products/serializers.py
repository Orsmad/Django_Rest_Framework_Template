from rest_framework import serializers
from .models import Product
from apps.profiles.models import Profile

class ProducteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product 
        fields = '__all__'

    def create(self, validated_data):

        # userz = 
        # print(type(userz))
        return Product.objects.create(**validated_data,profile=Profile.objects.get(user=self.context['user']  ))

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.image = validated_data.get('image', instance.image)
    #     instance.save()
    #     return instance
    