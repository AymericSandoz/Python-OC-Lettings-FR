import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_profiles_index_view(client, user, profile):
    """Test the profiles index view."""
    response = client.get(reverse('profiles:index'))
    assert response.status_code == 200
    assert len(response.context['profiles_list']) == 1


@pytest.mark.django_db
def test_profile_view(client, user, profile):
    """Test the profile detail view."""
    response = client.get(reverse('profiles:profile', args=[user.username]))
    assert response.status_code == 200
    assert response.context['profile'] == profile
