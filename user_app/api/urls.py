from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api import views


urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

]