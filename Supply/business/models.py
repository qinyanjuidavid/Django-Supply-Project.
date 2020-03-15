from django.db import models
from accounts.models import User,Categories



class Products(models.Model):
    product_name=models.CharField(max_length=56,verbose_name="Product Name")
    product_image=models.ImageField(upload_to="Products_Image",verbose_name="Image")
    price=models.FloatField(default=0.00,verbose_name="Price")
    discount_price=models.FloatField(blank=True,null=True,verbose_name='Discount Price')
    description=models.TextField(blank=True,null=True,verbose_name="Description")
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category} Category.'
    class Meta:
        verbose_name_plural="Products"
