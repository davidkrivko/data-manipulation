from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from users.filters import UserModelFilter
from users.models import UserModel, CategoryModel
from users.serializers import (
    UserModelSerializer,
    UserModelDetailSerializer,
    CategorySerializer,
)


class UserModelViewSet(viewsets.ModelViewSet):
    """
    Filter by:
        Favorite category
        Gender
        Birth date(exactly date)
        Age
        Age range (25-30)

    Pagination by 10 objects
    """

    queryset = UserModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserModelFilter

    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserModelDetailSerializer
        return UserModelSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    pagination_class = PageNumberPagination
    pagination_class.page_size = 10
