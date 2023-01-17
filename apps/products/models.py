from django.db import models
import uuid



from django.db import models
from apps.profiles.models import Profile

# Create your models here.
class Product(models.Model):
    id                  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name                = models.CharField(max_length=100,  blank=True, null=True)
    price               = models.IntegerField(blank=True, null=True)
    added_on            = models.DateTimeField(auto_now_add=True, editable=False)

    profile             = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, null=True,unique=False)
    image               = models.ImageField(null=True,blank=True,default='/placeholder.png')


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return (self.name)