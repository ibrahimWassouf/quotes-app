from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignUpView

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


class SignupTests(TestCase):

    #creates url object and its response template
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    #tests that the url works and the correct template is used
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign up')

    #tests to see whether response template has correct form and protection
    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    #tests to see whether correct view is used
    def test_signup_iew(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__,
        SignUpView.as_view().__name__)
