import csv
import datetime

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, views
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from main_app.settings import CACHE_TTL
from users.filters import UserModelFilter
from users.models import UserModel, CategoryModel
from users.serializers import (
    UserModelSerializer,
    UserModelDetailSerializer,
    CategorySerializer,
    EmailSerializer,
)
from users.tasks import send_email, generate_csv_file


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

    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserModelDetailSerializer
        return UserModelSerializer


class GetCSVUserDataApiView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserModelFilter

    def get(self, request, *args, **kwargs):
        """
        Upload csv file with users data.

        You can use
        """
        user_filter = UserModelFilter(request.GET, queryset=self.queryset)

        if user_filter.is_valid():
            filtered_data = user_filter.qs

            # Define CSV fieldnames
            fieldnames = [
                "first_name",
                "last_name",
                "email",
                "birth_date",
                "category",
            ]

            # Create a CSV response
            response = HttpResponse(content_type="text/csv")
            response["Content-Disposition"] = "attachment; filename=collected_data.csv"

            csv_writer = csv.DictWriter(response, fieldnames=fieldnames)
            csv_writer.writeheader()
            data_list = filtered_data.values(*fieldnames)
            csv_writer.writerows(data_list)

            return response
        else:
            return HttpResponse("Invalid filter criteria", status=400)


class SendEmailWithCSVFileApiView(views.APIView):
    queryset = UserModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserModelFilter

    def post(self, request):
        serializer = EmailSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get("email")

            user_filter = UserModelFilter(request.GET, queryset=self.queryset)
            if user_filter.is_valid():
                filtered_data = user_filter.qs
            
                data_list = list(filtered_data.values())
            
                filename = f"static/collected_data_{int(datetime.datetime.now().timestamp())}.csv"

                generate_csv_file.delay(filename, data_list)

                send_email.delay(
                    subject="Your Subject Here",
                    message="Your Message Here",
                    receivers=[email],
                    file_path=filename,
                )

                return Response(
                    {"message": "Email with CSV file is being sent!"},
                    status=200,
                )
            else:
                return Response(
                    {"error": "Invalid filter criteria"}, status=400
                )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    pagination_class = PageNumberPagination
    pagination_class.page_size = 10
