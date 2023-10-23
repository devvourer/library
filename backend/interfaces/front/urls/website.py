from django.urls import path

from interfaces.front.views import website as views

app_name = 'user'

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
]