from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, CreateStaffUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('create-staff/', CreateStaffUserView.as_view(), name='create-staff'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
