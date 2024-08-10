from django_filters.rest_framework import FilterSet
from .models import *
class ArticlFilter(FilterSet):
    class Meta:
        model =Articls
        fields = {'date':['exact'],
                  'title':['contains']}
        