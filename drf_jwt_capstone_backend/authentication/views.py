from django.contrib.auth import get_user_model
from django.http.response import Http404
from authentication.models import User
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, RegistrationSerializer, UserSerializer
from rest_framework import generics, serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Q
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

class UserList(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

class OfficerList(APIView):

    def get_object(self):
        try:
            return User.objects.filter(is_active=True)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        user = self.get_object()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
              

class UserDetail(APIView):
     
    def get_object(self, name):
        try:
            return User.objects.get(username=name)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, name):
        user = self.get_object(name)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, name):
        user = self.get_object(name)
        serializer = UserSerializer(user, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        user = self.get_object(name)
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class OfficerDetails(APIView):
    
    def get_object(self, name):
        try:
            return Officer.objects.get(username=name)
        except Officer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        officer = self.get_object(pk)
        serializer = UserSerializer(officer)
        return Response(serializer.data)


class SupervisorDetails(APIView):
    
    def get_object(self, name):
        try:
            return User.objects.get(username=name)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, name):
        user = self.get_object(name)
        serializer = UserSerializer(user)
        return Response(serializer.data)
