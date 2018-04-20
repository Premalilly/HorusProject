from rest_framework import serializers
from .models import Userapi

class UserapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userapi
        fields = ('name','email','mobile')