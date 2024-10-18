import pytest
from django.urls import reverse
from lettings.models import Letting


@pytest.mark.django_db
def test_lettings_index_view(client):
    """Test the lettings index view."""
    Letting.objects.create(title='Test Letting', address='123 Test St.')
    # Assurez-vous que le nom de l'URL est correct
    response = client.get(reverse('lettings:index'))
    assert response.status_code == 200
    assert 'lettings/index.html' in response.template_name[0]
    # Vérifie qu'un letting est dans la liste
    assert len(response.context['lettings_list']) == 1


@pytest.mark.django_db
def test_letting_view(client):
    """Test the letting detail view."""
    letting = Letting.objects.create(
        title='Test Letting', address='123 Test St.')
    # Assurez-vous que le nom de l'URL est correct
    response = client.get(reverse('lettings:letting', args=[letting.id]))
    assert response.status_code == 200
    assert response.context['title'] == letting.title
    assert response.context['address'] == letting.address
