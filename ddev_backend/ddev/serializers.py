from rest_framework import serializers
from ddev.models import *

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = '__all__'