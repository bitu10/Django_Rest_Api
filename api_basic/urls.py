from django.contrib import admin
from django.urls import path, include
from .views import GetApi
urlpatterns = [
    path('', GetApi.as_view(), name="get_api")
]