from rest_framework import serializers
from .models import Article, User, Saved, Query
from news import newssources


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'headline', 'link', 'source')

class SavedSerializer(serializers.ModelSerializer):
    user = serializers.RelatedField(source='user.user', read_only=True)
    article = ArticleSerializer(source='article', read_only=True)
    favourite = serializers.BooleanField(source='favourite')
    class Meta:
        model = Saved
        fields = ('user', 'favourite', 'id', 'headline', 'link', 'source')
