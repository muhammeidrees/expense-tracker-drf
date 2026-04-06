from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Transactions(models.Model):
    choices = (
        ("INCOME","Income"),
        ("EXPENSE","Expense"),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    type = models.CharField(max_length=10,choices=choices)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True)
    
    def __str__ (self):
        return f"{self.user.username} - {self.type} - {self.amount}"
    
    
    