from rest_framework import serializers, viewsets, permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import LoginUserSerializer, RegisterUserSerializer, UserSerializer
from django.contrib.auth.models import User

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()
    template_name = ''

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    queryset = User.objects.all()
    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)[1]
            }
        )

class UserAPI(generics.RetrieveAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user