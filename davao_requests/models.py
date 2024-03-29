from collections.abc import Collection
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import Personnel
# Create your models here.
class DavaoRequestHeader(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # id = models.BigAutoField(primary_key=True)
    rs_number = models.CharField(max_length=16, primary_key=True)
    particulars = models.CharField(max_length=100)
    payee = models.CharField(max_length=70, blank=True, null=True)
    project = models.CharField(max_length=150)
    urgent = models.BooleanField()
    note = models.CharField(max_length=165, null=True, blank=True)
    date_requested = models.DateField()
    date_needed = models.DateField()
    last_modified = models.DateField(auto_now_add=True)
    created = models.DateField(auto_now=True)


class DavaoRequestItems(models.Model):
    header = models.ForeignKey(DavaoRequestHeader, on_delete=models.CASCADE)
    item_id = models.CharField(max_length=100, blank=True)
    ignore = models.BooleanField(default=False)
    description = models.CharField(max_length=60)
    quantity = models.DecimalField(decimal_places=2, max_digits=10, blank=True, default=0)
    unit = models.CharField(max_length=20, blank=True)
    unit_cost = models.DecimalField(decimal_places=2, max_digits=10, blank=True, default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    served = models.BooleanField(default=False)

    def __str__(self):
        return self.header.rs_number


class AuthorizedPersons(models.Model):
    header = models.ForeignKey(DavaoRequestHeader, on_delete=models.CASCADE)
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE, related_name="AuthorizedPersonsDavao", null=True)
    # personnel = models.ManyToManyField(Personnel)
    name = models.CharField(max_length=53, null=True, blank=True)
    title = models.CharField(max_length=30, null=True, blank=True)
    signature = models.ImageField(upload_to='signatures/', blank=True)
    signed = models.BooleanField(null=True, default=False)

    def __str__(self):
        return f"{self.personnel.name} {self.personnel.title}"
    

class Monitoring(models.Model):
    header = models.ForeignKey(DavaoRequestItems, on_delete=models.CASCADE, null=True, blank=True)
    PO_no = models.CharField(max_length=100, null=True, blank=True)
    PO_date = models.DateField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    receiving_report = models.CharField(max_length=100, null=True, blank=True)
    DR_no = models.CharField(max_length=16, null=True, blank=True)
    SI_no = models.CharField(max_length=16, null=True, blank=True)
    OR_no = models.CharField(max_length=16, null=True, blank=True)
    CR_no = models.CharField(max_length=16, null=True, blank=True)
    withdrawal_no = models.CharField(max_length=16, null=True, blank=True)
    item_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=DavaoRequestItems)
def post_save_trigger(sender, instance, created, **kwargs):
    if created:
        Monitoring.objects.create(header=instance)
