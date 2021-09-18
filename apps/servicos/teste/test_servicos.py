import pytest
from django.urls import reverse
from apps.core.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('servicos:servico_detalhe', args=('redes'),))
    return resp


def test_stauscode(resp):
    assert resp.status_code == 200


