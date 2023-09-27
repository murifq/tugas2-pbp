link aplikasi adaptable: https://tokopakedi-tugas2.adaptable.app
# Tugas 2

## Implementasi Setiap Checklist yang Ada

#### Membuat sebuah proyek Django baru.
1. Membuat folder baru
2. Membuat _virtual environment_ dengan menjalankan ```python -m venv env```
3. Masuk ke dalam virtual environment dengan menjalankan ```env\Scripts\activate.bat```
4. Buat file `requirements.txt` yang berisi _dependencies_ yang diperlukan. File tersebut berisi
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
5. Membuat proyek Django yang baru bernama `tokopakedi` dengan menjalankan
    ```
    django-admin startproject tokopakedi .
    ```

### Membuat aplikasi dengan nama main pada proyek tersebut
1. Membuat aplikasi `main` baru dengan menjalankan 
    ```
    python manage.py startapp main
    ```
2. Mendaftarkan aplikasi `main` yang telah dibuat dengan membuka `settings.py` lalu tambahkan
    ```
        INSTALLED_APPS = [
        ...,
        'main',
        ...
        ]
    ```
### Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
1. Buka `urls.py` dalam direktori `tokopakedi` lalu tambahkan
    ```
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```
    url patterns admin digunakan agar bisa membuka admin site django. Sedangkan `main.urls` berguna agar aplikasi `main` dapat diakses

### Membuat model pada aplikasi main dengan nama Item
1. Buka `models.py` lalu tambahkan 
    ```
    class Item(models.Model):
    photo_url = models.CharField(max_length=512, default="https://static.vecteezy.com/system/resources/previews/005/337/799/original/icon-image-not-found-free-vector.jpg")
    name = models.CharField(max_length=255)
    amount =  models.IntegerField(default=0)
    price =  models.IntegerField(default=0)
    description = models.TextField()
    rating =  models.IntegerField(default=0)
    sold =  models.IntegerField(default=0)
    ```
2. Lakukan migrasi model dengan menjalankan
    ```
    python manage.py makemigrations
    ```
3. Menerapkan migrasi ke dalam basis data lokal dengan menjalankan 
    ```
    python manage.py makemigrations
    ```

### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
1. Buka `views.py` pada direktori `main` lalu tambahkan fungsi berikut
    ```
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
    ```
    Fungsi show_main berfungsi untuk mengembalikan `main.html` template jika dipanggil dan memberikan data melalui `context`.
    Fungsi show_home berfungsi untuk mengembalikan `home.html` template jika dipanggil dan memberikan data melalui `context`.
2. Tambahkan direktori `templates` di dalam direktori `main`. Direktori `templates` berguna untuk menyimpan template-template html file yang akan dipanggi jika diperlukan
3. Membuat `main.html` dan `home.html` sesuai dengan ketentuan. Hias sedikit dengan menggunakan css style

### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
1. Buat `urls.py` pada direktori main lalu tambahkan
    ```
    from django.urls import path
    from . import views

    app_name = 'main'

    urlpatterns = [
        path('', views.show_main, name='show_home'),
        path('home/', views.show_home, name='show_home'),
    ]
    ```
    http://127.0.0.1:8000/: memamnggil fungsi show_main pada views, lalu menampilkan `main.html`
    http://127.0.0.1:8000/home: memamnggil fungsi show_home pada views, lalu menampilkan `home.html`

### Melakukan deployment ke Adaptable
1. Simpan kode yang telah dibuat lalu diunggah ke github repository
2. Hubungkan Adaptable dengan github repository

## Bagan yang berisi request client ke web aplikasi berbasis Django
![Alt text](Django.jpg)

Berikut adalah alur responnya:
1. User request kepada `urls.py`
2. `urls.py` akan memanggil function di `views.py` sesuai dengan _pattern_ urlnya
3. `views.py` mengakses `models.py` untuk membaca atau menulis data ke _database_ melalui `models.py`
4. `views.py` juga mengakses berkas-berkas yang ada di `templates` untuk memanggil file-file yang sesuai (termasuk berkas-berkas `html`)
5. `views.py` mengembalikan response dengan data yang diambil dari `models.py` dan fiile-file yang ada di templates (termasuk `html`)

## Mengapa menggunakan _virtual environment_?
_Virtual environment_ digunakan untuk menjaga _dependencies_ yang dibutuhkan dari setiap proyek yang ada. Sebagai contoh jika kita mengerjakan banyak proyek django, maka kita bisa membedakan dan menjaga _dependencies_ dari setiap proyek yang ada. Bisa saja setiap proyek memiliki versi dan _dependencies_ yang berbeda-beda.

#Apakah bisa membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_?
Ya, tetap bisa. Namun tidak disarankan melakukan seperti itu. Hal tersebut akan sangat menyulitkan apabila misalkan, saat ini kita membuat proyek a. Lalu pada 3 tahun lagi, kita ingin mengubah proyek a kembali. Namun, sudah ada banyak pembaruan versi dari _dependencies_ yang kita gunakan. Sehingga bisa saja _packages_ yang kita miliki saat ini tidak sesuai dengan versi Django proyek 3 tahun yang lalu.

## Apakah itu MVC, MVT, MVVM dan perbedaannya?

### MVC (Model, View, Controller)
![Alt text](image.png)
(https://www.dicoding.com/blog/apa-itu-mvc-pahami-konsepnya/)

MVC adalah salah satu arsitektur dalam membuat aplikasi. Arsitektur ini memisahkan kode menjadi tiga bagian, yakni:
* Model: Mengatur segala hal yang berkaitan dengan data di dalam database
* View: Mengatur segala hal yang berkaitan dengan apa yang akan ditampilkan kepada pengguna dalam bentuk GUI. Sebagai contoh berkaitan dengan html dan css
* Controller: Sebgai jembatan antara model dan view

### MVT (Model, View, Template)
![Alt text](image-2.png)
(https://www.geeksforgeeks.org/django-project-mvt-structure/)

MVC adalah salah satu arsitektur dalam membuat aplikasi. Arsitektur ini memisahkan kode menjadi tiga bagian, yakni:
* Model: Mengatur segala hal yang berkaitan dengan data di dalam database
* b. View: Sebagai jembatan antara model dan template.
* Template: Mengatur segala hal yang berkaitan dengan apa yang akan ditamplkan kepada pengguna. Sebagai contoh berkaitan dengan html dan css

### MVVM (Model, View, View Model)
![Alt text](image-1.png)
(https://www.dicoding.com/blog/tips-design-pattern-mvvm/)

* Model: Mengatur segala hal yang berkaitan dengan data
* View: Mengatur segala hal yang berkaitan dengan apa yang akan ditampilkan kepada pengguna. Sebagai contoh berkaitan dengan html dan css
* View model: Berinteraksi dengan model lalu datanya diterukan ke view.

# Tugas 3

## Apa perbedaan antara form POST dan form GET dalam Django?
* POST
    1. Digunakan untuk mengirim data ke web server
    2. Sedikit lebih aman karena tidak terdapat data yang dikirim melalui URL.
    3. Tidak tersimpan di _browser_ _history_ dan _cache memory browser_
    4. POST _request_ tidak dapat di-_bookmark_ di _browser_

* GET
    1. Digunakan untuk membaca/mengambil data dari web server
    2. Sedikit tidak lebih aman karena terdapat data yang dikirim melalui URL
    3. Tersimpan di _browser_ _history_ dan _cache memory browser_
    4. GET _request_ dapat di-_bookmark_ di _browser_


## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
* XML
    1. XML adalah singkatan dari Extensible Markup Language
    2. Menggunakan konsep _tag_ dan _attribute_ dalam format datanya.
* JSON
    1. JSON adalah singkatan dari JavaScript Object Notation
    2. Menggunakan konsep_key and value_ dalama format datanya.
* HTML
    1. HTML adalah singkatan dari JHyperText Markup Language
    2. Menggunakan konsep _tag_ dan _attribute_ dalam format datanya.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
1. File JSON berukuran kecil sehingga dalam proses pertukaran data berjalan dengan cepat.
2. Format penulisan JSON lebih mudah dibaca oleh manusia, sehingga lebih mudah digunakan.
3. Hampir semua _browser_ yang populer digunakan saat ini mendukung penggunaan JSON.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Membuat input `form` untuk menambahkan objek model pada app sebelumnya
1. Membuat file `forms.py` yang akan digunakan untuk membuat struktur _form_ yang dapat digunakan untuk menerima data baru. 
```
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["photo_url", "name", "amount","price", "description", "rating","sold"]
```
2. Tambahkan _import_ yang dibutuhkan dalam file `views.py` yang ada pada folder `main`
```
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
```
3. Membuat fungsi `create_product` dalam file `views.py` dalam folder `main` yang akan dipanggil jika kita ingin menambahkan Item baru.
```
def create_product(request):
    form = ItemForm(request.POST or None)
    print(form)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_home'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
4. Ubah fungsi `show_main` dalam file `views.py` dalam folder `main` menjadi seperti berikut agar bisa menampilkan semua `Item` yang ada:
```
def show_main (request):
  template = loader.get_template('home.html')
  context = {
    "items":Item.objects.all().values(),
    "nama":"Muhamad Rifqi",
    "kelas":"PBP F",
    "nama_aplikasi":"tokopakedi"
  }   
  return HttpResponse(template.render(context, request))
```
5. Tambahkan kode berikut ke dalam `urls.py` dalam folder `main`
```
from main.views import show_main, create_product
```
6. Tambahkan _path_ baru ke dalam `urls.py` yang ada di dalam folder `main`
```
    . . .
    path('create-product', views.create_product, name='create_product'),
    . . .
```
7. Buat berkas _template_ HTML `create_product.html` yang baru di dalam folder `templates` 
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            margin: 0px;
        }
        h1, h2{
            color: white;
            text-align: left;
            margin: 5px;
        }
        header{
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            background-color: green;
            height: 125px;
            position: fixed;
            top: 0;
            min-width: 100%;
            /* z-index: 9999; */
        }
        main{
            display: flex;
            flex-direction: row;
            padding-top: 150px;
        }
        aside{
            flex: 3;
        }
        form{
            flex: 4;
        }
        .form-field{
            display: flex;
            flex-direction: column;
        }
        .form-field div{
            padding-left: 10px;
        }
        .form-field p{
            min-width: 120px;
            /* background-color: ; */
        }
        input{
            border-radius: 5px;
            border-color: grey;
            border-style: solid;
        }
    </style>
</head>
<body>
    <header>
        <div class="title">
            <h1>tokopakedi</h1>
        </div>
        <a class="create-product-button" href="{% url 'main:create_product' %}">
            <i class="fa fa-plus-circle" style="font-size:24px;color: white;"></i>
        </a>
    </header>

    <main>
        <form method="POST">
            {% csrf_token %}
            <table>
                <!-- {{ form.as_table }} -->
                <div class="form-field">
                    <p>Photo Url</p>
                    <div class="photo-url">{{form.photo_url}}</div>
                </div>
                <div class="form-field">
                    <p>Product Name</p>
                    <div class="name">{{form.name}}</div>
                </div>
                <div class="form-field">
                    <p>Amount</p>
                    <div class="amount">{{form.amount}}</div>
                </div>
                <div class="form-field">
                    <p>Price</p>
                    <div class="price">{{form.price}}</div>
                </div>
                <div class="form-field">
                    <p>Description</p>
                    <div class="description">{{form.description}}</div>
                </div>
                <div class="form-field">
                    <p>Rating</p>
                    <div class="rating">{{form.rating}}</div>
                </div>
                <div class="form-field">
                    <p>Sold</p>
                    <div class="sold">{{form.sold}}</div>
                </div>
                <tr>
                    <td></td>
                    <td>
                        <input type="submit" value="Add Product"/>
                    </td>
                </tr>
            </table>
        </form>
    </main>
</body>
</html>
```
8. Tambahkan `main.html` menjadi kode berikut agar bisa menampilkan semua `Item` yang ada
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">    
    <style>
        body{
            margin: 0px;
        }
        header{
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            background-color: green;
            height: 125px;
            position: fixed;
            top: 0;
            z-index: 9998;
            min-width: 100%;
        }
        .title{
            text-align: left;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding-left: 30px;
        }
        .create-product-button{
            padding-right: 30px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        h1, h2{
            color: white;
            text-align: left;
            margin: 5px;
        }
        .product-box{
            display: flex;
            border-radius: 10px;
            flex-direction: column;
            border-style: double;
            max-width:120px ;
        }
        .product-box p{
            padding-left: 2px;
            padding-right: 2px;
        }
        .price-field{
            font-weight: bold;
        }

        a{
            color: inherit;
            text-decoration: none;
        }
        img{
            max-width: 500px;
        }

        .review-container{
            display: flex;
            flex-direction: row;
        }
        .total-items{
            padding-top: 125px;
        }
        .items-container{
            display: flex;
            flex-direction: row;
            justify-content: start;
            flex-wrap: wrap;
            padding-top: 10px;
        }

    </style>
</head>
<body>
    
    <header>
        <h1>tokopakedi</h1>
        <a class="create-product-button" href="{% url 'main:create_product' %}">
            <i class="fa fa-plus-circle" style="font-size:24px;color: white;"></i>
        </a>
    </header>
    <div class="total-items">
        <p>Nama: {{nama}}</p>
        <p>Kelas: {{kelas}}</p>
        Terdapat {{items|length}} barang
    </div>
    <!-- {% if itemAdded != None %} -->
    <!-- {% endif %} -->
    <div class="items-container">
        {%for x in items%}
        <ul>
            <a href="">
                <div class="product-box">
                    <img src='{{x.photo_url}}' alt="">
                    <p>{{x.name}}</p>
                    <p class="price-field">Rp.{{x.price}}</p>
                    <div class="review-container">
                        <img src="https://cdn-icons-png.flaticon.com/512/2107/2107957.png" style="max-width: 12px; max-height: 12px;margin-top: 18px;">
                        <p>{{x.rating}} | </p>
                        <p>{{x.sold}} terjual</p>
                    </div>
                </div>
            </a>
        </ul>
        {% endfor %}
    </div>
</body>

</html>
```

### Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
1. Menambahkan fungsi `show_xml` di dalam `views.py` folder `main` yang berguna untuk menampilkan semua `Item` yang ada dalam bentuk xml
```
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
2. Menambahkan fungsi `show_json` di dalam `views.py` folder `main` yang berguna untuk menampilkan semua `Item` yang ada dalam bentuk JSON
```
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
3. Menambahkan fungsi `show_xml_by_id` di dalam `views.py` folder `main` yang berguna untuk menampilkan `Item` yang sesuai dengan `id` yang diminta dalam bentuk xml
```
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
4. Menambahkan fungsi `show_json_by_id` di dalam `views.py` folder `main` yang berguna untuk menampilkan `Item` yang sesuai dengan `id` yang diminta dalam bentuk JSON
```
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
5. Tambahkan fungsi `show_main` yang berguna untuk menampilkan semua `Item` yang ada dalam bentuk HTML (sudah ada di tugas sebelumnya, tetapi ada sedikit perubahan)
```
def show_main (request):
  template = loader.get_template('home.html')
  context = {
    "items":Item.objects.all().values(),
    "nama":"Muhamad Rifqi",
    "kelas":"PBP F",
    "nama_aplikasi":"tokopakedi"
  }   
  return HttpResponse(template.render(context, request))
```

### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
File `urls.py` yang ada di dalam folder `main` menjadi seperti berikut:
```
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_home'),
    path('create-product', views.create_product, name='create_product'),
    path('xml/', views.show_xml, name='show_xml'), 
    path('json/', views.show_json, name='show_xml'), 
    path('xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', views.show_json_by_id, name='show_json_by_id'), 
]
```
Penjelasan:
1. `path('', views.show_main, name='show_home'),` berguna untuk memanggil fungsi `show_main` yang ada di dalam `views.py` untuk menampilkan semua `Item` yang ada dalam bentuk HTML.
2. `path('create-product', views.create_product, name='create_product'),` berguna untuk memanggil fungsi `create_product` yang ada di dalam `views.py` untuk menambahakn `Item` baru.
3. `path('xml/', views.show_xml, name='show_xml'),` berguna untuk memanggil fungsi `show_xml` yang ada di dalam `views.py` untuk menampilkan semua `Item` yang ada dalam bentuk xml.
4. `path('json/', views.show_json, name='show_json'),` berguna untuk memanggil fungsi `show_json` yang ada di dalam `views.py` untuk menampilkan semua `Item` yang ada dalam bentuk JSON.
5. `path('xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),` berguna untuk memanggil fungsi `show_xml_by_id` yang ada di dalam `views.py` untuk menampilkan `Item` yang sesuai dengan `id` dalam bentuk xml.
6. `path('json/<int:id>/', views.show_json_by_id, name='show_json_by_id'),` berguna untuk memanggil fungsi `show_json_by_id` yang ada di dalam `views.py` untuk menampilkan `Item` yang sesuai dengan `id` dalam bentuk json.

## Mengakses URL menggunakan Postman
1. `main.html`
![Alt text](image-3.png)

2. XML
![Alt text](image-4.png)

3. JSON
![Alt text](image-5.png)

4. XML by id
![Alt text](image-6.png)

5. JSON by id
![Alt text](image-7.png)

## Bonus
Tambahkan kode berikut di bawah tag header dalam `main.html`
```
    <div class="total-items">
        <p>Nama: {{nama}}</p>
        <p>Kelas: {{kelas}}</p>
        Terdapat {{items|length}} barang
    </div>
```
Potongan kode tersebut berguna untuk menampilkan nama, kelas, dan juga total `Item` yang tersimpan.

# Tugas 4

## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah _built-in class_ Django yang berguna untuk membuat _user_. _Class_ ini memiliki beberapa _field_ bawaan seperti _username_, _password1_, dan _password2_ (yang berguna untuk konfirmasi _password_).

* Kelebihan Django UserCreationForm:
    1. Kita tidak perlu menulis banyak kode untuk membuat _user_. Kita bisa langsung menggunakan _class_ bawaan dari Django untuk membuat _user_.
    2. Terdapat beberapa fitur pengecekan dan kemanan bawaan. Seperti ketentuan _username_ dan _password_ yang dapat digunakan.
    3. Dapat meng-_handle_ _traffic_ yang cukup tinggi.
* Kekurangan Django UserCreationForm:
    1. Apabila proyek yang digunakan kecil, maka akan terlalu banyak hal yang harus dilakukan agar dapat menggunakan Django UserCreationForm.
    2. Harus belajar banyak hal baru yang berkaitan dengan Django UserCreationForm.

##  Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
* Autentikasi
    1. Proses pengecekan identitas untuk menentukan apakah seseorang itu _user_ atau bukan
    2. Proses memverifikasi _user_
    3. Dilakukan sebelum otorisasi
    4. Biasanya menggunakan _username_, _face recoginition_, _fingerprint_, dan lain-lain
    5. Data-data yang diberikan oleh _user_ dapat diubah oleh _user_

* Otorisasi
    1. Proses pengecekan akses apa saja yang dapat dilakukan oleh user
    2. Proses memvalidasi _user_
    3. Dilakukan setelah autentikasi
    4. Biasanya menggunakan _role user_ yang telah didefinisikan
    5. _User_ tidak dapat mengubah akses yang telah diberikan oleh pemilik sistem

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
* Cookies adalah data kecil yang dikirimkan oleh _web server_ kepada _browser_ yang berguna untuk menyimpan informasi kita sebagai user. Manfaatnya adalah jika kita membuka _website_ tersebut lagi, dapat meningkatkan pengalaman penggunaan. 
* Django memanfaat _cookies_ untuk menyimpan _Session ID_. _Session ID_ ini yang akan dikirmkan oleh _browser_ kepada _web server_ sehingga _website_ dapat menampilkan data yang diperlukan.Pendekatan seperti itu juga lebih aman karena _cookies_ hanya menyimpan _Session ID_.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Secara umum, _cookies_ aman digunakan dalam pengembangan _web_. Namun, bukan berarti tidak ada potensial risiko yang harus diwaspadai. Berikut adalah contoh risiko potensial penggunaan _cookies_:
1. Data di dalam _cookies_ bisa saja dicuri oleh _hacker_. Sehingga, _hacker_ dapat dapat mencuri identitas _user_. 
2. _Cookies_ juga mungkin saja tidak bekerja dengan baik pada semua jenis dan versi _browser_
3. _Cookies_ juga meningkatkan _bandwidth_ komunikasi antara _client_ dan _server_

## Implementasi Checklist

### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
* Implementasi registrasi
    1. Masuk ke dalam virtual environment
    2. Tambahkan _import_ berikut ke dalam `views.py`
    ```
    from django.shortcuts import redirect
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages 
    ```
    3. Tambahkan fungsi untuk registrasi pada `views.py` 
    ```
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
    ```
    4. Tambahkan HTML baru `register.html` di dalam `main/templates`
    ```
    {% extends 'base.html' %}

    {% block meta %}
        <title>Register</title>
        <style>
            body{
                margin: 0px;
            }

            .tokopakedi-h1{
                color: white;
                margin: 5px;
            }
            header{
                display: flex;
                flex-direction: row;
                justify-content:center;
                background-color: green;
                height: 125px;
                position: fixed;
                top: 0;
                min-width: 100%;
            }

            .login{
                padding-top: 250px;
                display: flex;
                flex-direction: row;
                justify-content: center;
            }
            .login-container{
                width: 300px;
                display: flex;
                flex-direction: column;
                box-shadow:0 0 2px 2px grey;
                border-radius: 10px;
                
                padding: 20px;
            }
            .login-field{
                margin-bottom: 20px;
            }
            input{
                width: 100%;
                height: 30px;
                border-radius: 10px;

            }
            .btn-login_btn{
                background-color: green;
                color: white;
            }
            .btn-login_btn:hover{
                cursor: pointer;
                color: whitesmoke;
                background-color: darkgreen;
            }
            
        </style>
    {% endblock meta %}

    {% block content %}  
    <header>
        <h1 class="tokopakedi-h1">tokopakedi</h1>
    </header>

    <div class = "login">
        <div class="login-container">

            <h1>Register</h1>  
        
                <form method="POST" >  
                    {% csrf_token %}  
                    <table>  
                        {{ form.as_div }}  
                        <tr>  
                            <div class="login-field">
                                <div class="username-field"></div>
                            </div>
                            <div class="login-field">
                                <div class="ppassword-field"></div>
                            </div>
                            <div class="login-field">
                                <div class="ppassword-confirmation-field"></div>
                            </div>
                            <input class="btn-login_btn" type="submit" name="submit" value="Daftar"/>
                            <p>Already registered? <a href="{% url 'main:login' %}">Login</a> </p>
                        </tr>  
                    </table>  
                </form>
        
            {% if messages %}  
                <ul>   
                    {% for message in messages %}  
                        <li>{{ message }}</li>  
                        {% endfor %}  
                </ul>   
            {% endif %}
        </div>

    </div>  

    {% endblock content %}
    ```
    5. Tambahkan _path url_ nya ke dalam `urls.py` yang ada di dalam `main`
    ```
    ...
        path('register/', views.register, name='register'),

    ...
    ```
* Implementasi _login_
    1. Tambahkan _import_ pada `views.py`
    ```
    from django.contrib.auth import authenticate, login
    ```
    2. Tambahkan fungsi _login_ pada `views.py`
    ```
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
    ```
    3. Tambahkan `login.html` pada `main/templates`
    ```
    {% extends 'base.html' %}

    {% block meta %}
        <title>Login</title>
        <style>
            body{
                margin: 0px;
            }
            .tokopakedi-h1{
                color: white;
                margin: 5px;
            }
            header{
                display: flex;
                flex-direction: row;
                justify-content:center;
                background-color: green;
                height: 125px;
                position: fixed;
                top: 0;
                min-width: 100%;
                /* z-index: 9999; */
            }

            .login{
                padding-top: 250px;
                display: flex;
                flex-direction: row;
                justify-content: center;
            }
            .login-container{
                width: 300px;
                display: flex;
                flex-direction: column;
                box-shadow:0 0 2px 2px grey;
                border-radius: 10px;
                
                padding: 20px;
            }
            .login-field{
                margin-bottom: 20px;
            }
            input{
                width: 100%;
                height: 30px;
                border-radius: 10px;

            }
            .btn-login_btn{
                background-color: green;
                color: white;
            }
            .btn-login_btn:hover{
                cursor: pointer;
                color: whitesmoke;
                background-color: darkgreen;
            }
            
        </style>
    {% endblock meta %}

    {% block content %}
    <header>
        <h1 class="tokopakedi-h1">tokopakedi</h1>
    </header>

    <div class = "login">

        <div class="login-container">

            <h1>Login</h1>
        
            <form method="POST" action="">
                {% csrf_token %}
                <table>
                    <div class="login-field">
                        <p>Username</p>
                        <input type="text" name="username" placeholder="Username" class="form-control">
                    </div>
                    <div class="login-field">
                        <p>Password</p>
                        <input type="password" name="password" placeholder="Password" class="form-control">
                    </div>
                    <input class="btn-login_btn" type="submit" value="Login">
                </table>
            </form>
        
            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}     
            <div class="register-container">
                <p>Don't have an account yet?</p>
                <a href="{% url 'main:register' %}">Register Now</a>
            </div>

        </div>

    </div>

    {% endblock content %}
    ```
    4. Tambahkan _path_ baru pada `urls.py`
    ```
    ...
    path('login/', views.login_user, name='login'), 
    ...
    ```
    5. Untuk meretriksi halaman _main_, tambahkan _import_ baru pada `views.py`
    ```
    from django.contrib.auth.decorators import login_required
    ```
    6. Tambahkan kode berikut di `views.py`
    ```
    ...
    @login_required(login_url='/login')
    def show_main(request):
    ...
    ```
* Implementasi _logout_
    1. Tambakan _import_ baru pada `views.py`
    2. Tambahkan fungsi _logout_ pada `views.py`
    ```
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```
    3. Tambahkan _hyperlink_ yang baru pada berkas `main.html`
    ```
    <a href="{% url 'main:logout' %}">
        <i class="fa fa-sign-out" style="font-size:24px;color: white;"></i>
    </a>
    ```
    4. Tambahkan _path_ baru pada `urls.py`
    ```
    ...
    path('logout/', views.logout_user, name='logout'),
    ...
    ```

## Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
1. Buka _register page_ pada aplikasi
2. Tambahkan user dengan ketentuan sebagai berikut:
    1) _username_: test, _password_: testdoang
    2) _username_: test2, _password_: test2doang
3. _Login_ pada tiap _user_, lalu tambahkan _item_ melalui _create product page_ dengan cara klik ikon tambah. Tambahkan _item_ sebanyak 3 pada masing-masing akun _user_ 


## Menghubungkan model Item dengan User.
1. Tambahkan _import_ baru di `models.py`
```
...
from django.contrib.auth.models import User
...
```
2. Tambahkan _field_ baru di `models.py`
```
...
class Item(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
...
```
3. Ubah fungsi `create_product` di `views.py` menjadi berikut
```
def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "create_product.html", context)
```
4. Ubah fungsi `show_main` di `views.py` menjadi berikut
```
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
```
5. Lakukan migrasi pada `models.py`
6. ![Alt text](image-8.png)
7. ![Alt text](image-9.png)

## Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
1. _Logout_ terlebih dahulu dari aplikasi jika sedang _login_
2. _Import_ kode berikut di `views.py`
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
3. Tambahkan potongan kode tersebut pada fungsi `login_user` di `views.py`
```
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```
4. Tambahkan kode tersebut pada `context` di `show_main` yang ada di `views.py`
```
...
'last_login': request.COOKIES['last_login'],
...
```
5. Tambahkan kode berikut pada fungsi `logout_user` di `views.py` untuk menghapus _cookies_ jika _logout_
```
...   
response.delete_cookie('last_login')
...
```
6. Tambagkan potongan kode berikut pada `main.html` untuk menginformasikan data _last login_ _user_

## Bonus
1. Tambahkan potongan kode berikut pada `product-box` di `main.html`
```
<div class="change-amount-btn">
    <form method="POST" action="{% url 'main:increase_amount' x.id %}">
        {% csrf_token %}
        <button type="submit" class="btn btn-success btn-sm">+1</button>
    </form>
    <form method="POST" action="{% url 'main:decrease_amount' x.id %}">
        {% csrf_token %}
        <button type="submit" class="btn btn-danger btn-sm">-1</button>
    </form>
    <form method="POST" action="{% url 'main:remove_item' x.id %}">
        {% csrf_token %}
        <button type="submit" class="btn btn-danger btn-sm">Del</button>
    </form>
</div>
```
Kode di atas ditambahkan agar apabila _button_ tertentu di klik, akan membuka _url_ tertentu dan akan meneruskan _id item_
2. Tambahkan fungsi berikut pada `views.py`
```
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
```
Fungsi di atas berguna untuk mendapatkan _item_ sesudai _id_ dan mengubah _amount_ dari _item_ sesuai dengan ketentuan
3. Tambahkann _path_ baru di `urls.py`
```
...
path('increase_amount/<int:id>/', views.increase_amount, name='increase_amount'),
path('decrease_amount/<int:id>/', views.decrease_amount, name='decrease_amount'),
path('remove_item/<int:id>/', views.remove_item, name='remove_item'),
...
```
_Path_ tersebut ditambahkan agar apabila terdapat pola _url_ yang diakses, maka fungsi di `views.py` dapat terpanggil