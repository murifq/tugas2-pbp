from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Item

# Create your views here.
def show_main (request):
  template = loader.get_template('main.html')
  context = {
    "nama":"Muhamad Rifqi",
    "kelas":"PBP F",
    "nama_aplikasi":"tokopakedi"
  }
  return HttpResponse(template.render(context, request))

def show_home (request):
  template = loader.get_template('home.html')
  context = {
    "items":Item.objects.all().values()
  }
  return HttpResponse(template.render(context, request))
