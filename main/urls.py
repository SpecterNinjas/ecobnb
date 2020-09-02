from django.urls import path
from main.views import register, main, place, activity, profile
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'main'
urlpatterns = [
    path('', main, name="main"),
    path('user_creation/', register, name='register'),
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'main/logout.html'), name='logout'),
    path('place/', place, name='place'),
    path('activity/', activity, name='activity'),
    path('profile/', profile, name='profile'),

]
