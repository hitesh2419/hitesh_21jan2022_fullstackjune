from rest_framework import serializers
from backend import models


class MovieSerializers(serializers.ModelSerializer):   
    class Meta:
        model=models.Movies
        fields='__all__'

class CastSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Cast
        fields='__all__'