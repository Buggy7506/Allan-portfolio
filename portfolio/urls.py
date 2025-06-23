from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('like/<int:pk>/', views.like_project, name='like_project'),
]
