from django.shortcuts import render #untuk memanggil file html
from django.http import HttpResponse #format html langsung ditulis di dalam httpresponse

def home(request):
    template_name = "home.html"
    return render(request, template_name)
