from django.test import TestCase
from .forms import AddItemForm
from .models import Item


class TestAddItemForm(TestCase):

    def setUp(self):
        Item.objects.get_or_create(name='Crossbow')
        self.item_instance = Item.objects.first()

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = AddItemForm({
            'item': self.item_instance.id,
            'quantity': '1',
        })
        self.assertTrue(form.is_valid(), msg="Form is valid")

    def test_form_invalid_item(self):
        """Test empty item field"""

        form = AddItemForm({
            'item': '',
            'quantity': 1
        })
        self.assertFalse(form.is_valid(), msg='Form is not valid')

    def test_form_invalid_quantity(self):
        """Test empty quantity, or below 0"""
        for validator in ['', 0]:
            form = AddItemForm({
                'item': self.item_instance.id,
                'quantity': validator
            })
        self.assertFalse(
            form.is_valid(),
            msg=f'Form is not valid if quantity value is {validator}')
