from django.urls import path, include
from rest_framework.routers import DefaultRouter
from transport.views import TransportViewSet

router = DefaultRouter()
router.register(r'transport', TransportViewSet, basename='transport')

urlpatterns = [
    path('', include(router.urls)),
]