from django.shortcuts import render

# Create your views here.

def landing_page(request):
    return render(
        request=request,
        template_name="iot_service/index.html",

    )