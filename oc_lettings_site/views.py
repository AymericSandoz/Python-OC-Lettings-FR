from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem.
# Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis.
# Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus.
# Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """Display the home page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    return render(request, 'index.html')


def error_404_view(request, exception):
    """Display the 404 error page.

    Args:
        request (HttpRequest): The request object.
        exception (Exception): The exception object.

    Returns:
        HttpResponse: The response object.
    """

    return render(request, '404.html', status=404)


def error_405_view(request, exception):
    """Display the 405 error page.

    Args:
        request (HttpRequest): The request object.
        exception (Exception): The exception object.

    Returns:
        HttpResponse: The response object.
    """
    return render(request, '405.html', status=405)
