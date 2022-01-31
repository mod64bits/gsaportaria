from django.test import Client, TestCase
from model_mommy import mommy
from django.conf import settings
from django.urls import reverse

from apps.users.models import User

class UserHomeTestCase(TestCase):
    pass


class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('users:register')

    def test_register_ok(self):
        data = {
            'username': 'mod64', 'password1': 'Teste*123', 'password2': 'Teste*123',
            'email': 'test@test.com'
        }
        resp = self.client.post(self.register_url, data)
        home_url = reverse('login')
        self.assertRedirects(resp, home_url)
        self.assertEquals(User.objects.count(), 1)

    def test_register_error(self):
        data = {'username': 'mod64', 'password1': 'teste123', 'password2': 'teste123'}
        resp = self.client.post(self.register_url, data)
        self.assertFormError(resp, 'form', 'email', 'Este campo é obrigatório.')


class UpdateUserTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:update_user')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_update_user_ok(self):
        data = {'name': 'test', 'email': 'test@test.com'}
        resp = self.client.get(self.url)
        self.assertEquals(resp.status_code, 302)
        self.client.login(username=self.user.username, password='123')
        resp = self.client.post(self.url, data)
        accounts_index_url = reverse('core:home')
        self.assertRedirects(resp, accounts_index_url)
        self.user.refresh_from_db()
        self.assertEquals(self.user.email, 'test@test.com')
        self.assertEquals(self.user.name, 'test')

    def test_update_user_error(self):
        data = {}
        self.client.login(username=self.user.username, password='123')
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')


class UpdatePasswordTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('users:update_password')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('Test**123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_update_password_ok(self):
        data = {
            'old_password': 'Test**123', 'new_password1': 'Test*123', 'new_password2': 'Test*123'
        }
        self.client.login(username=self.user.username, password='Test**123')
        resp = self.client.post(self.url, data)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('Test*123'))
