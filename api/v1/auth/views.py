from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from core.functions import api_response_data

class UserRegistrationView(APIView):
    permission_classes = []  

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            data = {
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            }
            return api_response_data(status_code=6000, message="User registered successfully", data=data)
        return api_response_data(status_code=6001, message="Registration failed", data=serializer.errors)

class UserLoginView(APIView):
    permission_classes = [] 

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            if user:
                refresh = RefreshToken.for_user(user)
                data = {
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh),
                }
                return api_response_data(status_code=6000, message="Login successful", data=data)
            return api_response_data(status_code=6001, message="Invalid credentials", data={})
        return api_response_data(status_code=6001, message="Invalid data", data=serializer.errors)