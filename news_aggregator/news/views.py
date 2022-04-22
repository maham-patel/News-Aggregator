from urllib import response
from news import newssources
import datetime
from django.utils.timezone import utc

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Article, User, Saved, Query
from .serializers import ArticleSerializer
from news import serializers

def home(request, format = None):
    return JsonResponse("Welcome to the news aggregator. Please enter a valid url", safe = False)

# Create your views here.
@api_view(['GET'])
def list(request, format = None):
    query_ = request.GET.get('query') or ''
    if query_ == "":
        Article_list = Article.objects.all()
        serializer = ArticleSerializer(Article_list, many = True)
        return Response(serializer.data)
    else:
        query_obj = Query.objects.get(query = query_)
        if (not query_obj):
            pass
        else:
            timedifference = (datetime.datetime.now(utc).replace(tzinfo=utc) - query_obj.date_of_query)    
            if timedifference.minutes <= 30:
                Article_list = query_obj.articles.all()
                serializer = ArticleSerializer(Article_list, many = True)
                return Response(serializer.data)
            else:
                # JsonResponse("Error: new data not found", safe = False)
                query_obj.delete()
                all_articles = newssources.get_news(query_)
                
                
                
                
        


def favourite(request, format = None):
    username = request.GET.get('user') or ''
    id = request.GET.get('pk') or ''
    if username == '' or id == '':
        return JsonResponse("Please enter a valid url", safe = False)
    elif username != "":
        string =  username + "'s "  + 'list of favourited news will be listed here'
        return JsonResponse(string, safe = False)
    else:
        string = username + "'s #" + str(id) + ' news has been favourited/unfavourited'
        return JsonResponse(string, safe = False)
