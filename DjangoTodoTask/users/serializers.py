from rest_framework import serializers
from users.models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id',
                 'title',
                 'description',
                 'created_at',
                 'completed')