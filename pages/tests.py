from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomepageTests(SimpleTestCase):

    #tests whether the link works, e.g., domain.com/ works
    def test_homepage_status_test(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    #tests whether path name returns correct url pattern
    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    #tests whether url pattern uses correct template
    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')