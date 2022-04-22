from rest_framework import serializers
from .models import Article, User, Saved, Query


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'headline', 'link', 'source')

class QuerySerializer(serializers.ModelSerializer):
    results = serializers.SerializerMethodField()
    class Meta:
        model = Query
        fields = ('query', 'results')
        
    # def get_results(self, obj):
    #     articles_set = Result.objects.filter(query=obj)
    #     serializer = ArticleSerializer(articles_set, many=True)
    #     return serializer
    
    def create(self, validated_data):
        articles_set = validated_data.pop('results')
        query_instance = Query.objects.create(**validated_data)
        article_serializer = ArticleSerializer(data=articles_set, many=True)
        if not article_serializer.is_valid():
            raise serializers.ValidationError(article_serializer.errors)
        article_serializer.save()
        
        
        
    

# class QuerySerializer(serializers.ModelSerializer):
#     articles = serializers.SerializerMethodField()
#     class Meta:
#         model = Query
#         fields = ('articles')
#     def get_articles(self, obj):
#         articles = obj.articles.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return serializer.data
#     def create(self, validated_data):
#         return Query.objects.create(**validated_data)

# class QueryResultSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Query_result
#         fields = ('query', 'article')

# class UserSavedArticlesUpdateSerializer(serializers.ModelSerializer):
#     # articles = 
        
# class UserSerializer(serializers.ModelSerializer):
#     article = 
#     class Meta:
#         model = user
#         fields = ('user')