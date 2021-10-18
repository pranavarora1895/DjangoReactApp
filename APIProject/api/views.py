from .models import Article
from django.contrib.auth.models import User
from .serializers import ArticleSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = (TokenAuthentication,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer