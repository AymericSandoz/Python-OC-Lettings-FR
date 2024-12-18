import pytest
from django.urls import reverse
from lettings.models import Letting
import logging


@pytest.mark.django_db
def test_lettings_index_view(client, letting_factory):
    """Test the lettings index view."""
    letting_factory(title='Test Letting', number=123)
    response = client.get(reverse('lettings:index'))
    assert response.status_code == 200
    assert len(response.context['lettings_list']) == 1


@pytest.mark.django_db
def test_letting_view(client, letting_factory):
    """Test the letting detail view."""
    letting = letting_factory(title='Test Letting', number=123)
    response = client.get(reverse('lettings:letting', args=[letting.id]))
    assert response.status_code == 200
    assert response.context['title'] == letting.title
    assert response.context['address'] == letting.address


@pytest.mark.django_db
def test_logging_lettings_index_view(client, caplog, letting_factory):
    """Test logging in the lettings index view."""
    letting_factory(title='Test Letting', number=123)

    with caplog.at_level(logging.INFO):
        client.get(reverse('lettings:index'))
        assert "User" in caplog.text
        assert "is requesting the lettings list" in caplog.text


@pytest.mark.django_db
def test_index_view_logging_error(client, caplog, monkeypatch):
    """Test that an error in the index view is logged correctly."""

    # Utilisation de `monkeypatch` pour simuler une exception dans `Letting.objects.all`
    def mock_all(*args, **kwargs):
        raise Exception("Test exception")

    monkeypatch.setattr(Letting.objects, "all", mock_all)

    with caplog.at_level(logging.ERROR):
        try:
            client.get(reverse('lettings:index'))
        except Exception:
            pass  # Ignore l'exception pour permettre de vérifier le log

        # Vérifie que le message d'erreur est bien dans les logs
        assert "Error Test exception" in caplog.text


@pytest.mark.django_db
def test_logging_letting_detail_view(client, caplog, letting_factory):
    """Test logging in the letting detail view."""
    letting = letting_factory(title='Test Letting', number=123)

    with caplog.at_level(logging.INFO):
        client.get(reverse('lettings:letting', args=[letting.id]))
        assert "User" in caplog.text
        assert f"is requesting the letting {letting.id}" in caplog.text


@pytest.mark.django_db
def test_logging_letting_detail_view_error(client, caplog):
    """Test logging an error in the letting detail view."""
    fake_id = 999911
    with caplog.at_level(logging.ERROR):
        response = client.get(reverse('lettings:letting', args=[fake_id]))
        assert response.status_code == 404
        assert f"Letting {fake_id} does not exist" in caplog.text
