import pytest
from django.urls import reverse
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_lettings_index_view(client):
    """Test the lettings index view."""
    address = Address.objects.create(
        number=123,
        street='Test St.q',
        city='Test City',
        state='TS',
        zip_code=12345,
        country_iso_code='TST'
    )

    Letting.objects.create(title='Test Letting', address=address)
    response = client.get(reverse('lettings:index'))
    assert response.status_code == 200
    # Vérifie qu'un letting est dans la liste
    assert len(response.context['lettings_list']) == 1


@pytest.mark.django_db
def test_letting_view(client):
    """Test the letting detail view."""
    address = Address.objects.create(
        number=123,
        street='Test St.q',
        city='Test City',
        state='TS',
        zip_code=12345,
        country_iso_code='TST'
    )
    letting = Letting.objects.create(
        title='Test Letting', address=address)
    response = client.get(reverse('lettings:letting', args=[letting.id]))
    assert response.status_code == 200
    assert response.context['title'] == letting.title
    assert response.context['address'] == letting.address
