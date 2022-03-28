from rest_framework import serializers
from .models import Profile, Home, Photo
from django.contrib.auth import get_user_model
from django.contrib.auth.models import  User
from rest_framework.authtoken.models import Token






class UserSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = User # tell django which model to use
        fields = ['id', 'username', 'password', 'first_name', 'last_name' ] # tell djan
        extra_kwargs = {'password': {'write_only': True, 'required' : True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class ProfileSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Profile # tell django which model to use
        fields = ('id', 'user', 'userphoto', 'status') # tell djan


# class UserSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
#     class Meta:
#         model = User # tell django which model to use
#         fields = ('id', 'username', 'password', 'email', 'firstname', 'lastname', 'userphoto', 'status') # tell djan


class HomeSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Home # tell django which model to use
        fields = ('id', 'owner', 'type','street', 'city', 'state', 'coverphoto','rent', 'beds', 'baths', 'garage', 'description',) # tell djan


class PhotoSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Photo # tell django which model to use
        fields = ('id', 'home', 'photos',) # tell dja
