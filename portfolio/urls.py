from django.urls import path
from . import views

urlpatterns = [
    # -------------------------
    # Ping URL
    # -------------------------
    path("ping/", views.ping, name="ping"),
    path('', views.index, name='index'),
    path('like/<int:pk>/', views.like_project, name='like_project'),
]
