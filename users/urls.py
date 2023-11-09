from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import UserModelViewSet, CategoryViewSet

router = DefaultRouter()
router.register("users", UserModelViewSet)
router.register("categories", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "users"
