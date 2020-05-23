from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from .views import HomePageView,AboutPageView


class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('pages:home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        """Проверка корректности адреса"""
        self.assertEqual(self.response.status_code,200)

    def test_page_template(self):
        """Проверка того, что заданный адрес возвращает нужную страницу"""
        self.assertTemplateUsed(self.response,'home.html')

    def test_page_contains_correct(self):
        """Проверка того, что есть текст Homepage"""
        self.assertContains(self.response, 'Homepage')

    def test_page_does_not_incorrect_contains(self):
        """Проверка того, что на странице нет заданного текста"""
        self.assertNotContains(
            self.response,'Hi there! I should not be in the page'
        )

    def test_page_url_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )

class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('pages:about')
        self.response = self.client.get(url)

    def test_page_status_code(self):
        """Проверка корректности адреса"""
        self.assertEqual(self.response.status_code,200)

    def test_page_template(self):
        """Проверка того, что заданный адрес возвращает нужную страницу"""
        self.assertTemplateUsed(self.response,'about.html')

    def test_page_contains_correct(self):
        """Проверка того, что есть текст Homepage"""
        self.assertContains(self.response, 'About Page')

    def test_page_does_not_incorrect_contains(self):
        """Проверка того, что на странице нет заданного текста"""
        self.assertNotContains(
            self.response,'Hi there! I should not be in the page'
        )

    def test_page_url_pageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )
