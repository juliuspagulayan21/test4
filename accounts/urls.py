from django.urls import path
from .views import SignUp, ProfileDetailView

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
]