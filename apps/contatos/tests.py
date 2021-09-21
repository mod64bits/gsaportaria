from django.test import TestCase
from .forms import ContatoForm


class ContatoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/contato/')

    def test_get(self):
        """Get /contato/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_contato(self):
        """Must use /contato_form.html"""
        self.assertTemplateUsed(self.resp, 'contato/contato_form.html')

    def test_html(self):
        """Html must contain input tags"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 7)
        self.assertContains(self.resp, 'type="text"', 4)
        self.assertContains(self.resp, 'type="email"')

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, ContatoForm)

    def test_form_has_fields(self):
        """Form must have  fields."""
        form = self.resp.context['form']
        self.assertSequenceEqual(['nome', 'email', 'telefone', 'assunto', 'mensagem'], list(form.fields))

    def test_form_has_text_area(self):
        """Form must have  fields."""
        form = self.resp.context['form']
        self.assertSequenceEqual(['nome', 'email', 'telefone', 'assunto', 'mensagem'], list(form.fields))

