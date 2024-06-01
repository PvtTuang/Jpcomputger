from django.db import models
from posts.models import Product

class SalesHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField()
    sold_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - Quantity: {self.quantity_sold} - Sold at: {self.sold_at}"
    
