from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('profile_list/',views.profile_list, name= 'profile_list'),
    path('profile/<int:pk>', views.profile, name= 'profile'),
    path('login_user/',views.login_user, name = 'login_user'),
    path('logout_user/',views.logout_user, name = 'logout_user'),
    path('register_user/',views.register_user, name = 'register_user'),
    path('update_user/',views.update_user, name = 'update_user'),
]
