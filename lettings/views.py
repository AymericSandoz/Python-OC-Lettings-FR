from django.shortcuts import render
from django.views.decorators.http import require_GET
from .models import Letting
import logging
from django.http import Http404

# Aenean leo magna, vestibulum et tincidunt fermentum,
# consectetur quis velit.
# Sed non placerat massa. Integer est nunc,
# pulvinar a tempor et, bibendum id arcu.
# Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;
# Cras eget scelerisque
# test

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@require_GET
def index(request):
    """Display lettings list.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    try:
        lettings_list = Letting.objects.all()
        logger.info(
            f"User {request.user.username} is requesting the lettings list")

    except Exception as e:
        logger.error(f"Error {e} for user " +
                     f"{request.user.username} when accessing lettings list")
        raise
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta
# nisl id eleifend. Praesent dignissim, odio eu consequat pretium, purus urna
# vulputate arcu, vitae efficitur lacus justo nec purus. Aenean finibus faucibus
# lectus at porta. Maecenas auctor, est ut luctus congue, dui enim mattis enim,
# ac condimentum velit libero in magna. Suspendisse potenti. In tempus a nisi
# sed laoreet. Suspendisse porta dui eget sem accumsan interdum. Ut quis urna
# pellentesque justo mattis ullamcorper ac non tellus. In tristique mauris eu
# velit fermentum, tempus pharetra est luctus. Vivamus consequat aliquam libero,
# eget bibendum lorem. Sed non dolor risus. Mauris condimentum auctor elementum.
# Donec quis nisi ligula. Integer vehicula tincidunt enim, ac lacinia augue
# pulvinar sit amet.

@require_GET
def letting(request, letting_id):
    try:
        logger.info(
            f"User {request.user.username} is requesting the letting {letting_id}")
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        logger.error(
            f"Letting {letting_id} does not exist for user {request.user.username}")
        raise Http404("Letting does not exist")
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
