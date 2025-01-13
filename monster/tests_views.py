from django.test import TestCase
from django.urls import reverse
from .models import Monster


class MonsterLibraryTest(TestCase):
    def setUp(self):
        Monster.objects.create(
            name="Hobgoblin",
            description="A large type of goblin, with savage fangs.")
        Monster.objects.create(
            name="Dragon",
            description="A firebreathing lizard with wings.")
        Monster.objects.create(
            name="Ent",
            description="A living tree, they are wise and peaceful creatures.")

    def test_monster_library(self):
        url = reverse('monster_library')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monster/monster_library.html')
        self.assertIn('monsters', response.context)
        self.assertEqual(len(response.context['monsters']), 3)
        self.assertContains(response, 'Hobgoblin')
        self.assertContains(response, 'Dragon')
        self.assertContains(response, 'Ent')
