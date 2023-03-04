from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

# All possible urls from the domain name (can redirect to other urls in applications)
urlpatterns = [
    path('bots/', include('bots.urls')),
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
