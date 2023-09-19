from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Item
from main.forms import ItemForm
from django.urls import reverse
from django.core import serializers

def show_main (request):
  template = loader.get_template('main.html')
  context = {
    "items":Item.objects.all().values(),
    "nama":"Muhamad Rifqi",
    "kelas":"PBP F",
    "nama_aplikasi":"tokopakedi"
  }   
  return HttpResponse(template.render(context, request))

def create_product(request):
    form = ItemForm(request.POST or None)
    print(form)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")