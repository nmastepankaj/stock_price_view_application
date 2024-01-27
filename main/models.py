from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    """Model for Company"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}   {self.id}"

class Stock(models.Model):
    """Model for Stock"""
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField()
    open = models.FloatField()
    close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    last = models.FloatField()
    prev_close = models.FloatField()
    no_trades = models.IntegerField()
    no_of_shrs = models.IntegerField()
    net_turnover = models.FloatField()

    def __str__(self):
        return self.company.name
    
class FavouriteStock(models.Model):
    """Model for Favourite Stock"""
    user = models.ForeignKey(User, on_delete=models.CASCADE) # commented because we are not using any authentication
    stock = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} {self.stock.name}"