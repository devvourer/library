from rest_framework.routers import DefaultRouter
from rest_framework import permissions

from django.urls import include, path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from interfaces.api.views.library import LibraryViewSet, CommentViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Library API",
      default_version='v1',
      description="Library description",
      terms_of_service="https://www.google.com/policies/terms/",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register('book', LibraryViewSet, 'book')
router.register('comment', CommentViewSet, 'comment')

urlpatterns = [
    path('api/', include(router.urls)),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
