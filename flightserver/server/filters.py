import django_filters
from .models import Flight, Specification


class FlightFilter(django_filters.FilterSet):
    # title = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Flight
        fields = {
            'msn': ['exact', 'icontains'],
            'airport': ['icontains']
        }
