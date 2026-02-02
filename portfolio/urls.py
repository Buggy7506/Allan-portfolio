from django.urls import path
from . import views

urlpatterns = [
    # -------------------------
    # Ping URL
    # -------------------------
    path("ping/", views.ping, name="ping"),
    path('', views.index, name='index'),
    path('project/<int:pk>/like/', views.like_project_ajax, name='like_project_ajax'),
]
