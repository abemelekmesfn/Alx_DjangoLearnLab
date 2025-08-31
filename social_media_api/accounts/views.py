from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from posts.models import Post


# Create your views here.
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email,
            'bio': user.bio,
            'followers': user.followers.count(),
            'following': user.following.count(),
        })

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        users = CustomUser.objects.all()
        target_user = get_object_or_404(users, id=user_id)
        if target_user == request.user:
            return Response({"error": "You cannot follow yourself."}, status=400)

        request.user.following.add(target_user)
        return Response({"message": f"You are now following {target_user.username}."}, status=200)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        users = CustomUser.objects.all()
        target_user = get_object_or_404(users, id=user_id)
        request.user.following.remove(target_user)
        return Response({"message": f"You have unfollowed {target_user.username}."}, status=200)

