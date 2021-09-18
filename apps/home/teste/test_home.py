import pytest
from django.urls import reverse
from apps.core.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('home:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>GSA Portaria</title>')


def test_whatsApp(resp):
    assert_contains(resp, '(19) 99345-6524')


def test_email(resp):
    assert_contains(resp, 'gilsimar@gsaportaria.com.br')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("home:home")}">GSA')
