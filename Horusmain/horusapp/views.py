# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets
from .models import Userapi
from .serializers import UserapiSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework import views
from rest_framework.response import Response
from django.contrib.auth.models import User
import jwt, json
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class UserapiViewSet(viewsets.ModelViewSet):
    queryset = Userapi.objects.all()
    serializer_class = UserapiSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    #authentication_classes = (TokenAuthentication,)

