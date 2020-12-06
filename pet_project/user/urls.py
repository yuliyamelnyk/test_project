from django.urls import path
from .views import UserAPIView, PostAPIView, CreateListPostAPIView

urlpatterns = [
    path("user", UserAPIView.as_view()), 
    path("post/<pk>", PostAPIView.as_view()),
    path("post/", CreateListPostAPIView.as_view())
]
