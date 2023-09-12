from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from .models import Item
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/home/')
        self.assertTemplateUsed(response, 'home.html')

    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')
    
    def setUp(self):
        Item.objects.create(
            photo_url="test",
            name="AK-47",
            amount = 1,
            price = 1,
            description="description",
            rating = 5,
            sold = 5
        )
        
    def test_item(self):
        ak47 = Item.objects.get(name="AK-47")
        self.assertEqual(ak47.price, 1)