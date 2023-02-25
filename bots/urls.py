from django.urls import path

from . import views

# All possible urls after the domain-name/bots
app_name = 'bots'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/vote', views.VoteView.as_view(), name='vote'),
    path('<int:pk>/update', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.RemoveView.as_view(), name='remove'),
]