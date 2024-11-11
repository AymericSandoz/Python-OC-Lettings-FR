import pytest
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User
import logging


@pytest.mark.django_db
def test_profiles_index_view(client):
    """Test the profiles index view."""
    user = User.objects.create_user(username='testuser', password='testpass')
    Profile.objects.create(user=user, favorite_city='Test City')
    # Assurez-vous que le nom de l'URL est correct
    response = client.get(reverse('profiles:index'))
    assert response.status_code == 200
    # Vérifie qu'un profile est dans la liste
    assert len(response.context['profiles_list']) == 1


@pytest.mark.django_db
def test_profile_view(client):
    """Test the profile detail view."""
    user = User.objects.create_user(username='testuser', password='testpass')
    profile = Profile.objects.create(user=user, favorite_city='Test City')
    # Assurez-vous que le nom de l'URL est correct
    response = client.get(reverse('profiles:profile', args=[user.username]))
    assert response.status_code == 200
    assert response.context['profile'] == profile


@pytest.mark.django_db
def test_index_view_logging_error(client, caplog, monkeypatch):
    """Test that an error in the index view is logged correctly."""

    # Utilisation de `monkeypatch` pour simuler une exception dans `Letting.objects.all`
    def mock_all(*args, **kwargs):
        raise Exception("Test exception")

    monkeypatch.setattr(Profile.objects, "all", mock_all)

    with caplog.at_level(logging.ERROR):
        try:
            client.get(reverse('profiles:index'))
        except Exception:
            pass  # Ignore l'exception pour permettre de vérifier le log

        # Vérifie que le message d'erreur est bien dans les logs
        assert "Error Test exception" in caplog.text


@pytest.mark.django_db
def test_logging_profiles_detail_view_error(client, caplog):
    """Test logging an error in the letting detail view."""
    fake_name = 'fake_name'
    with caplog.at_level(logging.ERROR):
        response = client.get(reverse('profiles:profile', args=[fake_name]))
        assert response.status_code == 404
        assert f"Profile {fake_name} does not exist" in caplog.text
