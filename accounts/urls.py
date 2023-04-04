from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.LogoutUser.as_view(), name='logout_user'),
]