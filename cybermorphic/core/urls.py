from django.urls import path

from cybermorphic.core import views

app_name = "core"
urlpatterns = [
    path("", views.LandingView.as_view(), name="landing"),
]
