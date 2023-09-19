from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["photo_url", "name", "amount","price", "description", "rating","sold"]