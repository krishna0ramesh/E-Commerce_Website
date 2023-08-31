from django.db import models

# Create your models here.
class items(models.Model):
    item_name=models.CharField(max_length=20) 
    items_description=models.TextField()

    def __str__(self):
        return self.item_name

class ceramics(models.Model):
    ceramic_name=models.CharField(max_length=20)
    ceramic_id=models.CharField(max_length=20,null = True,unique=True)
    ceramic_img=models.ImageField(upload_to='products',null=True)
class planters(models.Model):
    planter_name=models.CharField(max_length=20)
    planter_id=models.CharField(max_length=20,null = True,unique=True)
    planter_img=models.ImageField(upload_to='products',null=True)
class candles(models.Model):
    candle_name=models.CharField(max_length=20)
    candle_id=models.CharField(max_length=20,null = True,unique=True)
    candle_img=models.ImageField(upload_to='products',null=True)
class cards(models.Model):
    card_name=models.CharField(max_length=20)
    card_id=models.CharField(max_length=20,null = True,unique=True)
    card_img=models.ImageField(upload_to='products',null=True)

class orders(models.Model):
    recipient=models.CharField(max_length=20)
    phno=models.CharField(max_length=10)
    email=models.EmailField()
    item_name=models.ForeignKey(items,on_delete=models.CASCADE)
    uid=models.CharField(max_length=20)
    customize=models.TextField(null=True)
    num=models.IntegerField()
    bookedOn=models.DateField(auto_now=True)