from rest_framework import serializers
from .models import User, Post

from datetime import datetime


# class Comment:
#     def __init__(self, email, content, created=None):
#         self.email = email
#         self.content = content
#         self.created = created or datetime.now()


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id', 'email', 'text']


# class CommentSerializer(serializers.Serializer):
    # email = serializers.EmailField()
    # content = serializers.CharField(max_length=200)
    # created = serializers.DateTimeField(read_only=True)

    # def validate(self, data):
    #     if data['email'] == 'tes@gmail.com':
    #         raise serializers.ValidationError('LOL')
    #     super().validate(data)
    #     return data

    # def create(self, validated_data):
    #     instance = Comment(**validated_data)
    #     return instance

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
