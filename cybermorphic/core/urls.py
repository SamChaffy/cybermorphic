from  django.urls import path
from cybermorphic.core import views
from rest_framework import routers

from rest_framework import routers
router = routers.SimpleRouter()

app_name='core'
router.register(r'contact', views.ContactMessageViewSet, basename='contact')
urlpatterns = router.urls

urlpatterns += [
    path("", views.LandingView.as_view(), name='landing'),
]
