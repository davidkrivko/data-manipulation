import django_filters
from .models import UserModel
from datetime import datetime, timedelta


class UserModelFilter(django_filters.FilterSet):
    age = django_filters.NumberFilter(
        field_name="age",
        method="filter_by_age",
        label="Age",
    )

    age_range = django_filters.CharFilter(
        field_name="age_range",
        method="filter_by_age_range",
        label="Age Range (e.g., 25-30 years)"
    )

    class Meta:
        model = UserModel
        fields = {
            "category": ["exact"],
            "gender": ["exact"],
            "birth_date": ["exact"],
        }

    def filter_by_age(self, queryset, name, value):
        today = datetime.today()

        value = float(value)
        max_value = today - timedelta(days=int(value * 365.25))
        min_value = today - timedelta(days=int((value + 1) * 365.25))

        return queryset.filter(birth_date__gte=min_value, birth_date__lt=max_value)

    def filter_by_age_range(self, queryset, name, value):
        try:
            start_age, end_age = map(int, value.split("-"))
        except ValueError:
            return queryset
    
        today = datetime.today()

        start_age = float(start_age)
        end_age = float(end_age)
        max_value = today - timedelta(days=int(start_age * 365.25))
        min_value = today - timedelta(days=int((end_age + 1) * 365.25))
    
        return queryset.filter(
            birth_date__gte=min_value, birth_date__lte=max_value
        )
