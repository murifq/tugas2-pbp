from django.contrib import admin

# Register your models here.
from .models import Item

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("name", "price", "amount",)
  
admin.site.register(Item, MemberAdmin)