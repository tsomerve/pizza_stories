from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('', views.all, name='all'),
]