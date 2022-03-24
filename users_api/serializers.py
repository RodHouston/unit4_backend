from rest_framework import serializers
from .models import User, Home, Photo

class UserSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = User # tell django which model to use
        fields = ('id', 'name', 'password', 'email', 'firstName', 'lastName',) # tell djan


class HomeSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Home # tell django which model to use
        fields = ('id', 'owner', 'type','street', 'city', 'state',) # tell djan


class PhotoSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Photo # tell django which model to use
        fields = ('id', 'home', 'photos',) # tell dja
