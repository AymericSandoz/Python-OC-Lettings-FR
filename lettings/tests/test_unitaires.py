import logging
import pytest
from django.urls import reverse
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_logging_letting_detail_view_error(client, caplog):
    """Test logging an error in the letting detail view."""
    fake_id = 999911
    with caplog.at_level(logging.ERROR):
        response = client.get(reverse('lettings:letting', args=[fake_id]))
        assert response.status_code == 404
        assert f"Letting {fake_id} does not exist" in caplog.text


@pytest.mark.django_db
def test_get_lettings_view(client):
    """Test getting lettings."""
    response = client.get(reverse('lettings:index'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_letting_view(client, letting_factory):
    """Test getting a letting."""
    letting = letting_factory(title='Test Letting', number=123)
    response = client.get(reverse('lettings:letting', args=[letting.id]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_lettings_view_not_found(client):
    """Test getting a letting that does not exist."""
    response = client.get(reverse('lettings:letting', args=[9999]))
    assert response.status_code == 404


@pytest.mark.django_db
def test_get_lettings_object(client, address_factory):
    """Test getting lettings object."""
    lettings = []
    for i in range(10):
        address = address_factory(number=123 + i)
        letting = Letting.objects.create(title=f'Test Letting {i}', address=address)
        lettings.append(letting)

    response = client.get(reverse('lettings:index'))

    assert len(response.context['lettings_list']) == 10
    for i in range(10):
        assert response.context['lettings_list'][i].title == f'Test Letting {i}'
        assert response.context['lettings_list'][i].address == lettings[i].address
