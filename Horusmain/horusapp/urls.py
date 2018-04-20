from rest_framework import routers
from .views import UserapiViewSet
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'Userdetails', UserapiViewSet)

urlpatterns = [
    url(r'^api/', include('rest_framework.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
]

urlpatterns += router.urls