import pytest
from django.contrib.auth.models import User
from profiles.models import Profile
from lettings.models import Address, Letting


@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpass')


@pytest.fixture
def profile(user):
    return Profile.objects.create(user=user, favorite_city='Test City')


@pytest.fixture
def address_factory():
    def create_address(number):
        return Address.objects.create(
            number=number,
            street='Test St.q',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TST'
        )
    return create_address


@pytest.fixture
def letting_factory(address_factory):
    def create_letting(title, number):
        address = address_factory(number=number)
        return Letting.objects.create(title=title, address=address)
    return create_letting
