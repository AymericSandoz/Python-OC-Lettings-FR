# middleware.py
from django.http import HttpResponseNotAllowed
from django.shortcuts import render


class MethodNotAllowedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if isinstance(response, HttpResponseNotAllowed):
            return render(request, '405.html', status=405)
        elif response.status_code == 404:
            return render(request, '404.html', status=404)
        return response
