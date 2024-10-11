from django.contrib import admin
from django.urls import path, include

from . import views

# Configuration des gestionnaires d'erreurs
handler404 = 'oc_lettings_site.views.error_404_view'
handler405 = 'oc_lettings_site.views.error_405_view'


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
