from django.views.generic import RedirectView
from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(
            url=settings.STATIC_URL + "favicon.ico",
            permanent=True
        ),
    ),
    # -------------------------
    # Ping URL
    # -------------------------
    path("ping/", views.ping, name="ping"),
    path('', views.index, name='index'),
    path('project/<int:pk>/like/', views.like_project_ajax, name='like_project_ajax'),
]
