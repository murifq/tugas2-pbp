from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('create-product', views.create_product, name='create_product'),
    path('xml/', views.show_xml, name='show_xml'), 
    path('json/', views.show_json, name='show_json'), 
    path('xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', views.show_json_by_id, name='show_json_by_id'), 
    
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'), 
    path('logout/', views.logout_user, name='logout'),
    
    path('increase_amount/<int:id>/', views.increase_amount, name='increase_amount'),
    path('decrease_amount/<int:id>/', views.decrease_amount, name='decrease_amount'),
    path('remove_item/<int:id>/', views.remove_item, name='remove_item'),

    path('get-product/', views.get_product_json, name='get_product_json'),
    path('create-product-ajax/', views.add_product_ajax, name='add_product_ajax'),

path('create-flutter/', views.create_product_flutter, name='create_product_flutter'),
]