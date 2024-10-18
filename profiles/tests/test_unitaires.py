import pytest
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profiles_index_view(client):
    """Test the profiles index view."""
    user = User.objects.create_user(username='testuser', password='testpass')
    Profile.objects.create(user=user, favorite_city='Test City')
    # Assurez-vous que le nom de l'URL est correct
    response = client.get(reverse('profiles:index'))
    assert response.status_code == 200
    assert 'profiles/index.html' in response.template_name[0]
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
