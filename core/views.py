from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

# Create your views here.

class ProductAPIView(APIView):

    # permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication, SessionAuthentication]

    def get(self, request):
        book = Product.objects.all()
        serializer = ProductSerializer(book, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
