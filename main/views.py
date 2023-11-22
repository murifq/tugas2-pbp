import json
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Item
from main.forms import ItemForm
from django.urls import reverse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout 
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='/login')
def show_main (request):
    items = Item.objects.filter(user=request.user)
    template = loader.get_template('main.html')
    context = {
        "items":items,
        "name":request.user.username,
        "nama_aplikasi":"tokopakedi",
        'last_login': request.COOKIES['last_login'],
        }   
    return HttpResponse(template.render(context, request))

def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def increase_amount(request, id):
    item = get_object_or_404(Item, pk=id)
    item.amount += 1
    item.save()
    return redirect('main:show_main')

def decrease_amount(request, id):
    item = get_object_or_404(Item, pk=id)
    if(item.amount > 0):
        item.amount -= 1
    item.save()
    return redirect('main:show_main')

def remove_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('main:show_main')



def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        user = request.user
        print("Line 119")
        photo_url = request.POST.get("photo_url")
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        price = request.POST.get("price")
        description = request.POST.get("description")
        rating = request.POST.get("rating")
        sold = request.POST.get("sold")

        new_product = Item(photo_url = photo_url, name=name, amount = amount, price=price, description=description, rating = rating,sold = sold, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()


from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


    
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            photo_url = data["photourl"],
            name = data["name"],
            amount = int(data["amount"]),
            price = int(data["price"]),
            description = data["description"],
            rating = int(data["rating"]),
            sold = int(data["sold"]),


        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)