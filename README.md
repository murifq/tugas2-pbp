link aplikasi adaptable: https://tokopakedi-tugas2.adaptable.app

A. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    #GitHub Setting:
        1. Membuat repository GitHub dengan nama "tugas2-pbp".
        2. Membuat folder direktori lokal.
        3. Melakukan "git init"
        4. Melakukan konfigurasi username dan email
        5. Melakukan "git branch -M main"
        6. Melakukan "git remote add origin <Link_Repo>
        7. Menambahkan file .gitignore (berisi apa saja yang akan diabaikan Git) dan requiremnts.txt (berisi apa saja yang akan diinstall)
    
    #Membuat Virtual environment:
        1. Jalankan "python -m venv env"
        2. Jalnakan "env\Scripts\activate.bat"

    #Membuat Django:
        1. Lakukan "pip install -r requirements.txt"
        2. Membuat proyek Django yang baru dengan melakukan ```django-admin startproject tokopakedi .```
        3. Buka settings.py lalu tambahkan : 
        ```ALLOWED_HOSTS = ["*"]```
        Hal tersebut dilakukan agar bisa diakses oleh semua host.
        4. Buat aplikasi main baru dengan menjalankan ```python manage.py startapp main```
        5. Buka settings lalu tambahkan aplikasi main dengan cara berikut: 
        ```
        INSTALLED_APPS = [
            ...,
            'main',
            ...
        ]
        ```
        6. Membuat model dengan nama Item di dalam kelas models.py. models.py berisi:
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
        Setiap field model memliki tipe datanya dan default valuenya masing-masing.
        7. Melakukan migrasi model dengan menjalankan ```python manage.py makemigrations``` lalu ```python manage.py migrate```
        8.

#Implementasi Setiap Checklist yang Ada

##Membuat sebuah proyek Django baru.
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

##Membuat aplikasi dengan nama main pada proyek tersebut
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
##Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
1. Buka `urls.py` dalam direktori `tokopakedi` lalu tambahkan
    ```
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```
    url patterns admin digunakan agar bisa membuka admin site django. Sedangkan `main.urls` berguna agar aplikasi `main` dapat diakses

##Membuat model pada aplikasi main dengan nama Item
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

##Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
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

##Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
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

##Melakukan deployment ke Adaptable
1. Simpan kode yang telah dibuat lalu diunggah ke github repository
2. Hubungkan Adaptable dengan github repository

#Bagan yang berisi request client ke web aplikasi berbasis Django


#Mengapa menggunakan _virtual environment_?
_Virtual environment_ digunakan untuk menjaga _dependencies_ yang dibutuhkan dari setiap proyek yang ada. Sebagai contoh jika kita mengerjakan banyak proyek django, maka kita bisa membedakan dan menjaga _dependencies_ dari setiap proyek yang ada. Bisa saja setiap proyek memiliki versi dan _dependencies_ yang berbeda-beda.

#Apakah bisa membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_?
Ya, tetap bisa. Namun tidak disarankan melakukan seperti itu. Hal tersebut akan sangat menyulitkan apabila misalkan, saat ini kita membuat proyek a. Lalu pada 3 tahun lagi, kita ingin mengubah proyek a kembali. Namun, sudah ada banyak pembaruan versi dari _dependencies_ yang kita gunakan. Sehingga bisa saja _packages_ yang kita miliki saat ini tidak sesuai dengan versi Django proyek 3 tahun yang lalu.

#Apakah itu MVC, MVT, MVVM dan perbedaannya?

##MVC (Model, View, Controller)
![Alt text](image.png)
(https://www.dicoding.com/blog/apa-itu-mvc-pahami-konsepnya/)
MVC adalah salah satu arsitektur dalam membuat aplikasi. Arsitektur ini memisahkan kode menjadi tiga bagian, yakni:
a. Model: Mengatur segala hal yang berkaitan dengan data di dalam database
b. View: Mengatur segala hal yang berkaitan dengan apa yang akan ditampilkan kepada pengguna dalam bentuk GUI. Sebagai contoh berkaitan dengan html dan css
c. Controller: Sebgai jembatan antara model dan view

##MVT (Model, View, Template)
![Alt text](image-2.png)
(https://www.geeksforgeeks.org/django-project-mvt-structure/)
MVC adalah salah satu arsitektur dalam membuat aplikasi. Arsitektur ini memisahkan kode menjadi tiga bagian, yakni:
a. Model: Mengatur segala hal yang berkaitan dengan data di dalam database
b. View: Sebagai jembatan antara model dan template.
c. Template: Mengatur segala hal yang berkaitan dengan apa yang akan ditamplkan kepada pengguna. Sebagai contoh berkaitan dengan html dan css

##MVVM (Model, View, View Model)
![Alt text](image-1.png)
(https://www.dicoding.com/blog/tips-design-pattern-mvvm/)
a. Model: Mengatur segala hal yang berkaitan dengan data
b. View: Mengatur segala hal yang berkaitan dengan apa yang akan ditampilkan kepada pengguna. Sebagai contoh berkaitan dengan html dan css
c. View model: Berinteraksi dengan model lalu datanya diterukan ke view.