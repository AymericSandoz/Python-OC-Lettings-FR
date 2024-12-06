from django.shortcuts import render
from django.views.decorators.http import require_GET
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem.
# Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis.
# Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus.
# Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.


@require_GET
def index(request):
    """Display the home page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    # log info pour user request.user.username
    try:
        logger.info(
            f"User {request.user.username} is requesting the homepage")
        return render(request, 'index.html')
    except Exception as e:
        logger.error(f"Error {e} for user {request.user.username}")
        raise
