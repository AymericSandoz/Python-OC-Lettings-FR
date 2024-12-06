from django.shortcuts import render
from django.views.decorators.http import require_GET
from .models import Profile
import logging
from django.http import Http404

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# sed consequat libero pulvinar eget. Fuscfaucibus, urna quis auctor pharetra,
# massa dolor cursus neque, quis dictum lacus d


@require_GET
def index(request):
    """Display the profiles list.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    try:
        profiles_list = Profile.objects.all()
        logger.info(
            f"User {request.user.username} is requesting the profiles list")
    except Exception as e:
        logger.error(f"Error {e} for user {request.user.username}")
        raise
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)

# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males


@require_GET
def profile(request, username):
    """Display a user profile.

    Args:
        request (HttpRequest): The request object.
        username (str): The username of the profile to display.

    Returns:
        HttpResponse: The response object.
    """
    try:
        profile = Profile.objects.get(user__username=username)
        logger.info(
            f"User {request.user.username} is requesting the profile {username}")
    except Profile.DoesNotExist:
        logger.error(
            f"Profile {username} does not exist for user {request.user.username}")
        raise Http404("Profile does not exist")
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
