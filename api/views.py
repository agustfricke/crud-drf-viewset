from rest_framework import viewsets
from .serializers import BlogSerializer, UserSerialzier
from .models import Blog, User

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerialzier
    queryset = Blog.objects.all()

class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
