from django.db import models
from django.contrib.auth.models import User

class Cryptocurrency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=10)
    price_per_unit = models.DecimalField(max_digits=20, decimal_places=10)
    date_added = models.DateTimeField(auto_now_add=True)
