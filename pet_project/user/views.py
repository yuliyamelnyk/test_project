from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
from .serializers import UserSerializer, PostSerializer
from .models import User, Post



class UserAPIView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field='email'

class ru(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field='id'

class PostAPIView(generics.CreateAPIView,):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# class UserAPIView(APIView):

#     def get(self, request, *args, **kwargs):
#         comment = Comment(email='leila@example.com', content='foo bar')
#         serializer = CommentSerializer(comment)
#         return Response({'message':serializer.data})

#     def post(self, request, *args, **kwargs):
#         serializer = CommentSerializer(data=self.request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
#         return Response(serializer.data)

    # def put(self, request, *args, **kwargs):
    #     comment = Comment(email='leila@example.com', content='foo bar')
    #     serializer = CommentSerializer(data=self.request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(comment, serializer.v)
    #     return Response({'message':'put'})

    # def patch(self, request, *args, **kwargs):
    #     return Response({'message':'patch'})

    # def delete(self, request, *args, **kwargs):
        # return Response({'message':'delete'})