from rest_framework import serializers
from .models import Article, User, Saved, Query
from news import newssources


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'headline', 'link', 'source')

class QuerySerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(source = 'articles', many=True)
    class Meta:
        model = Query
        fields = ('articles')

class SavedSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(source = 'savedarticles', many=True)
    class Meta:
        model = Saved
        fields = ('article', 'favourite')

class UserSerializer(serializers.ModelSerializer):
    articles = SavedSerializer(source = 'saved', many=True)
    
    class Meta:
        model = User
        fields = ('articles')
