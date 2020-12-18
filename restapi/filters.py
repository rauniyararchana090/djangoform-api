import django_filters
from .models import *

class AirportFilter(django_filters.FilterSet):
    class Meta:
        model= Airport
        fields='__all__'
