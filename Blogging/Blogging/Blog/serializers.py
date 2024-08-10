from .models import Articls
from rest_framework import serializers

class ArticlSerialaizer(serializers.ModelSerializer):
    class Meta : 
        model = Articls
        fields = '__all__'
