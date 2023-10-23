from django.urls import include, path

from interfaces.front.urls import (
    users,
    website
)

urlpatterns = [
    path('', include(website, namespace='website')),
    path('user/', include(users, namespace='user')),

]