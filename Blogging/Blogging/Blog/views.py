from django.shortcuts import render
from rest_framework import mixins, generics
from .models import Articls
from rest_framework.viewsets import ModelViewSet 
from .serializers import  ArticlSerialaizer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter , OrderingFilter
from .filters import ArticlFilter

class ArticlList(generics.ListCreateAPIView):
    queryset = Articls.objects.all()
    serializer_class = ArticlSerialaizer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = ArticlFilter
    search_fields = ['title']
    ordering_fields = ['title']

class ArticlDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articls.objects.all()
    serializer_class =ArticlSerialaizer    
