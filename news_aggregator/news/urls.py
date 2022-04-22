from django.contrib import admin
from django.urls import path
from news import views
from rest_framework.urlpatterns import format_suffix_patterns

appname = 'news'
urlpatterns = [
    path('', views.home, name='home'),
    path('/', views.list, name='list'),
    path('/favourite', views.favourite, name='favourite'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)