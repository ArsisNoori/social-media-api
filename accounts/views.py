from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from django.contrib.auth.password_validation import validate_password
User = get_user_model()
# Create your views here.

class RegisterView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password:
            return Response(
                {'error': 'Please provide both username and password'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            validate_password(password)
        except ValidationError as e:
            return Response(
                {'error': e.messages},
                status=status.HTTP_400_BAD_REQUEST
            )
        if User.objects.filter(username=username).exists():
            return Response(
                {'error': 'User with this username already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if User.objects.filter(email=email).exists():
            return Response(
                {'error': 'Email with this email already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        user = User.objects.create_user(username=username, password=password, email=email )
        return Response(
            {'message': 'User created successfully.', 'username': user.username},
            status=status.HTTP_201_CREATED
        )



