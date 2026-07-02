from django.db import models
from categories.models import Category
from user.models import User
from bigcategory.models import BigCategory


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="products",null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    big_category = models.ForeignKey(BigCategory, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    incoming_price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField(default=0)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_data = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name