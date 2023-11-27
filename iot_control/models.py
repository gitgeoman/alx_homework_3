import random
import string
from django.db import models


# Create your models here.

class Device(models.Model):
    id = models.CharField(
        auto_created=True, 
        default = "".join(random.choices(string.ascii_uppercase, k=12)), 
        primary_key=True, 
        max_length=15
        )
    typ = models.CharField(max_length=15)
    status = models.CharField(max_length=15)
    message = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)


    