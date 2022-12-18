from django.test import TestCase
from .models import MyTable

class FirstTestUser(TestCase):
    def setUp(self):
        MyTable.objects.create(name="Anna", email="exam@ex.com", age="20")
        MyTable.objects.create(name="Yulia", email="example@example.com", age="44")
    def testUserData(self):
        anya=MyTable.objects.get(name="Anna")
        yulia=MyTable.objects.get(name="Yulia")

        self.assertEqual(anya.user_data(), 'Имя пользователя: Anna, почта: exam@ex.com, возраст: 20')
        self.assertEqual(yulia.user_data(), 'Имя пользователя: Yulia, почта: example@example.com, возраст: 44')
# Create your tests here.
