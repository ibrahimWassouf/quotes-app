from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'aib',
            email = 'aib2@hotmail.com',
            password = '123passtest'
        )

        self.assertEqual(user.username, 'aib')
        self.assertEqual(user.email, 'aib2@hotmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username = 'aib',
            email = 'aib@hotmail.com',
            password = '123passtest'
        )

        self.assertEqual(user.username, 'aib')
        self.assertEqual(user.email, 'aib@hotmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)