from django.db import models

# Create your models here.
class DavaoAuthorizedPersons(models.Model):
    firstname = models.CharField(max_length=60)
    middle_initial = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    role = models.CharField(max_length=60)

class CotabatoAuthorizedPersons(models.Model):
    firstname = models.CharField(max_length=60)
    middle_initial = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    role = models.CharField(max_length=60)

class NegrosAuthorizedPersons(models.Model):
    firstname = models.CharField(max_length=60)
    middle_initial = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    role = models.CharField(max_length=60)

class SurigaoAuthorizedPersons(models.Model):
    firstname = models.CharField(max_length=60)
    middle_initial = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    role = models.CharField(max_length=60)


class Personnel(models.Model):
    name = models.CharField(max_length=53)
    title = models.CharField(max_length=30)
    signature = models.ImageField(upload_to='signatures/', blank=True)

    def __str__(self):
        return self.name