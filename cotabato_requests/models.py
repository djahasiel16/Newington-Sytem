from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CotabatoRequestHeader(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    rs_number = models.CharField(max_length=100)
    particulars = models.CharField(max_length=200)
    payee = models.CharField(max_length=150)
    project = models.CharField(max_length=100)
    urgent = models.BooleanField()
    date_requested = models.DateField()
    date_needed = models.DateField()
    last_modified = models.DateField(auto_now_add=True)
    created = models.DateField(auto_now=True)

class CotabatoRequestItems(models.Model):
    rs_number = models.ForeignKey(CotabatoRequestHeader, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20)
    unit_cost = models.IntegerField()
    amount = models.IntegerField()
    served = models.BooleanField()