from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.inventory.views import ItemViewSet

router = DefaultRouter()
router.register('items',ItemViewSet,basename='item')

urlpatterns = []

urlpatterns += router.urls