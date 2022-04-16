from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserCreate, UserDetail

urlpatterns = [
    path("users/", UserCreate.as_view(), name="register"),
    path("users/<int:pk>/", UserDetail.as_view(), name='detail'),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
