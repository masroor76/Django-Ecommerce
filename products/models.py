from django.db import models

# Create your models here.
class ProductsModel(models.Model):
    ProductName = models.CharField(max_length=150)
    ProductDescription = models.TextField()
    ProductPrice = models.FloatField()
    StockCount = models.IntegerField(10)
    onSale = models.BooleanField(default=False)

    def __str__(self):
        return self.ProductName