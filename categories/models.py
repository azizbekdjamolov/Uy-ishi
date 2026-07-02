from django.db import models
from bigcategory.models import BigCategory

class Category(models.Model):
    big_category = models.ForeignKey(BigCategory,on_delete=models.CASCADE,related_name='categories',null=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name