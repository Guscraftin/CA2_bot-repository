from django.contrib import admin
from django.urls import include, path

# All possible urls from the domain name (can redirect to other urls in applications)
urlpatterns = [
    path('bots/', include('bots.urls')),
    path('admin/', admin.site.urls),
]
