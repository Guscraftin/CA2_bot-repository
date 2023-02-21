from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('bots/', include('bots.urls')),
    path('admin/', admin.site.urls),
]