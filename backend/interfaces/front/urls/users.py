from django.urls import path

from interfaces.front.views import users as views

app_name = 'user'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('sign-up/', views.Register.as_view(), name='register'),
    path('verify_email/', views.VerifyEmail.as_view(), name='verify_email'),

]

