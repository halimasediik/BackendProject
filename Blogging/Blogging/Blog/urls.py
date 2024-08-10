from django.urls import path ,include
from . import views
from .views import ArticlList

urlpatterns = [
    path('articl/',views.ArticlList.as_view()),
     path('articl/<int:pk>/',views.ArticlDetail.as_view()),
]
