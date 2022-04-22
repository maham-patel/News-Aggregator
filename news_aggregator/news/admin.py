from django.contrib import admin
from .models import Article, User, Saved, Query

admin.site.site_header = 'News Aggregator Admin'

class AdminNewsArticle(admin.ModelAdmin):
    list_display = ('id', 'headline', 'link', 'source')
    list_display_links = ('id', 'headline')
    list_filter = ('source',)
    search_fields = ('headline', 'source')
    list_per_page = 25
    
class AdminUser(admin.ModelAdmin):
    list_display = ('user',)
    list_display_links = ('user',)
    list_filter = ('user',)
    search_fields = ('user',)
    list_per_page = 25
    
class AdminUserSavedArticle(admin.ModelAdmin):
    list_display = ('user', 'article', 'favourite')
    list_display_links = ('user', 'article')
    list_filter = ('user', 'article', 'favourite')
    search_fields = ('user', 'article')
    list_per_page = 25
    
class AdminQuery(admin.ModelAdmin):
    list_display = ('query', 'date_of_query')
    list_display_links = ('query', 'date_of_query')
    list_filter = ('query', 'date_of_query')
    search_fields = ('query', 'date_of_query')
    list_per_page = 25
    
# Register your models here.
admin.site.register(Article, AdminNewsArticle)
admin.site.register(User, AdminUser)
admin.site.register(Saved, AdminUserSavedArticle)
admin.site.register(Query, AdminQuery)
