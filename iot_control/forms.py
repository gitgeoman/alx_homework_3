from django import forms 
from . import models

class DeviceForm(forms.ModelForm):
    class Meta:
        model = models.Device
        # fields = ['typ', 'status', 'message' ]
        fields = '__all__'