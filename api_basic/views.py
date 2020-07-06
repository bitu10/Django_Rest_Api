from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
# Create your views here.

class GetApi(ListAPIView):
      def get(self, request, format=None):
        qs = User.objects.all()
        serializer = UserSerializer(qs, many=True)
        jsonresp = {
            "ok" : True,
            "members" : serializer.data

        }
        return Response(jsonresp)
