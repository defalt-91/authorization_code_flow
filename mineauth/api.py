from django.urls import path, include
from django.contrib.auth.models import User, Group
from django.contrib import admin

admin.autodiscover()

from rest_framework import generics, permissions, serializers, views

from oauth2_provider.contrib.rest_framework import (
	IsAuthenticatedOrTokenHasScope,
	OAuth2Authentication,
	TokenHasReadWriteScope,
	TokenHasScope,
)


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email', "first_name", "last_name")


class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ("name",)


# Create the API views
class UserList(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
	permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset = User.objects.all()
	serializer_class = UserSerializer


class GroupList(generics.ListAPIView):
	permission_classes = [permissions.IsAuthenticated, TokenHasScope]
	required_scopes = ['groups']
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class SongView(views.APIView):
	authentication_classes = [OAuth2Authentication]
	permission_classes = [IsAuthenticatedOrTokenHasScope]
	required_scopes = ['music']
	required_alternate_scopes = {
			"GET"   : [["read"]],
			"POST"  : [["create"], ["post", "widget"]],
			"PUT"   : [["update"], ["put", "widget"]],
			"DELETE": [["delete"], ["scope2", "scope3"]],
	}
