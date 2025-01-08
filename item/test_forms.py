from django.test import TestCase
from .forms import AddItemForm
from .models import Item

class TestAddItemForm(TestCase):

    def setUp(self):
        Item.objects.get_or_create(name='Crossbow')

    def test_form_is_valid(self):
        """ Test for all fields"""

        item_instance = Item.objects.first()

        form = AddItemForm({
            'item': item_instance.id,
            'quantity': '1',
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")