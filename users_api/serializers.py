from rest_framework import serializers
from .models import User, Home

class UserSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = User # tell django which model to use
        fields = ('id', 'name', 'password', 'email',) # tell djan


class HomeSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Home # tell django which model to use
        fields = ('id', 'owner', 'type','street', 'city', 'state',) # tell djan
