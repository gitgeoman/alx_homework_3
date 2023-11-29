import random
import string
from django.db import models
from enum import Enum, auto


# Create your models here.


class Device(models.Model):
    id = models.CharField(
        auto_created=True,
        default="".join(random.choices(string.ascii_uppercase, k=12)),
        primary_key=True,
        max_length=15
    )
    msg_type = [
        ("SWITCH_ON", "SWITCH_ON"),
        ("SWITCH_OFF", "SWITCH_OFF"),
        ("CHANGE_COLOR", "CHANGE_COLOR"),
        ("PLAY_SONG", "PLAY_SONG"),
        ("OPEN", "OPEN"),
        ("CLOSE", "CLOSE"),
    ]
    device_type = models.CharField(max_length=15)
    status = models.CharField(max_length=15)
    message_type = models.CharField(max_length=15, choices=msg_type)
    message = models.TextField()

    updated_at = models.DateTimeField(auto_now_add=True)
