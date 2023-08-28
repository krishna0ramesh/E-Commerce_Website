from django.db import models

# Create your models here.
class items(models.Model):
    item_name=models.CharField(max_length=20) 
    items_description=models.TextField()
class ceramics(models.Model):
    ceramic_name=models.CharField(max_length=20)
    ceramic_id=models.IntegerField
    ceramic_img=models.ImageField(upload_to='products')