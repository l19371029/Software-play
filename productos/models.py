from django.db import models

# Cración de los modelos referente a la app de producto.

class Product(models.Model):
    nameProduct = models.CharField(max_length=30)
    descriptionProduct = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nameProduct
