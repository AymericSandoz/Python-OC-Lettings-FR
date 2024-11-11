import pytest
from django.urls import reverse
import logging


@pytest.mark.django_db
def test_error_404_view(client):
    """Test the custom 404 error view."""
    response = client.get('/nonexistent-url/')
    assert response.status_code == 404
    assert b'404 - Page Not Found' in response.content
    assert b'Sorry, the page you are looking for does not exist.' in response.content


@pytest.mark.django_db
def test_error_405_view(client):
    """Test the custom 405 error view."""
    response = client.post(reverse('lettings:index'))
    assert response.status_code == 405
    assert b'405 - Method Not Allowed' in response.content
    assert b'Sorry, the method is not allowed for the requested URL.' in response.content


@pytest.mark.django_db
def test_index_view(client):
    """Test the home page view."""
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert b'Welcome to Holiday Homes' in response.content
    assert b'Privacy Policy' in response.content


@pytest.mark.django_db
def test_logging_index_view_info(client, caplog):
    """Test logging of info level in the index view."""
    with caplog.at_level(logging.INFO):
        # Effectuer une requête GET vers la vue 'index'
        response = client.get(reverse('index'))
        username = response.wsgi_request.user.username

        # Vérifier que le code de réponse est 200
        assert response.status_code == 200

        # Vérifier que le message d'info attendu est dans les logs
        assert f"User {username} is requesting the home page" in caplog.text
