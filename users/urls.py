from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import (
    UserModelViewSet,
    CategoryViewSet,
    GetCSVUserDataApiView,
    SendEmailWithCSVFileApiView,
)

router = DefaultRouter()
router.register("users", UserModelViewSet)
router.register("categories", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "export_csv/",
        GetCSVUserDataApiView.as_view(),
        name="export_csv",
    ),
    path(
        "export_csv/email/",
        SendEmailWithCSVFileApiView.as_view(),
        name="csv-email",
    )
]

app_name = "users"
