from rest_framework import serializers
from .models import ScribbleQuest_User, Maths_Score, Words_Score

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScribbleQuest_User
        fields = '__all__'
