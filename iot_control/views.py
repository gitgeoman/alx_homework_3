import random
import string
from django.shortcuts import redirect, render

from iot_control.forms import DeviceForm

from . import models
# Create your views here.

def landing_page(request):
    return render(
        request=request,
        template_name="iot_service/index.html",
    )


def device_list(request):
    return render(
        request=request,
        template_name = 'iot_service/devices.html',
        context = {'devices': models.Device.objects.all().values()},
    )


def device_add(request):
    form = DeviceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('devices')
    return render(
        request=request, 
        template_name='iot_service/device_add.html', 
        context={"form":form}
        )
    
def delete(request, id ):
    device = models.Device.objects.get(id=id)
    device.delete()
    return redirect('devices')

def update(request, id ):
    device = models.Device.objects.get(id=id)
    form = DeviceForm(request.POST or None, instance=device)
    if form.is_valid():
        form.save()
        return redirect('devices')
    return render(
        request = request, 
        template_name='iot_service/device_upd.html', 
        context={'form':form}
        )