from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet

router = DefaultRouter()
router.register('cats', CatViewSet, basename='cats')

urlpatterns = [
   path('', include(router.urls)),
]
