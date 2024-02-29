from django.db import models

# Create your models here.
class Personnel(models.Model):
    name = models.CharField(max_length=53)
    title = models.CharField(max_length=30)
    signature = models.ImageField(upload_to='signatures/personnel/', blank=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} {self.name}"