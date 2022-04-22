from news import newssources
import datetime
from django.utils.timezone import utc

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse

from .models import Article, User, Saved, Query
from .serializers import ArticleSerializer
from news import serializers

def home(request, format = None):
    return JsonResponse("Welcome to the news aggregator. Please enter a valid url", safe = False)

# Create your views here.
@api_view(['GET'])
def list(request, format = None):
    " List all articles or Queried Articles"
    #get the params for the request, if it hits then we will query based on the params, else we will list all articles
    query_ = request.GET.get('query') or ''
    if query_ == "":
        Article_list = Article.objects.all()
        serializer = ArticleSerializer(Article_list, many = True)
        return Response(serializer.data)
    else:
        try:
            #get the query object
            query_obj = Query.objects.get(query = query_)
            #calculate the time difference between last query call and current time
            timedifference = (datetime.datetime.now(utc).replace(tzinfo=utc) - query_obj.date_of_query)
            #if the time difference is greater than the time limit, then we will call the apis again
            #else we will return the queried articles    
            if timedifference.total_seconds() > 3600:
                Article_list = Article.objects.filter(query = query_obj)
                serializer = ArticleSerializer(Article_list, many = True)
                return Response(serializer.data)
            else:
                #delete old query object
                query_obj.delete()
                #create a new query object
                query_obj = Query.objects.create(query = query_)
                #call the api again
                articles_result = newssources.get_news(query_)
                #create the articles
                for article in articles_result:
                    Article.objects.create(query = query_obj, headline = article['headline'], link = article['link'], source = article['source'])
                #get the queried articles
                Article_list = Article.objects.filter(query = query_obj)
                #serialize the queried articles and return the response
                serializer = ArticleSerializer(Article_list, many = True)
                return Response(serializer.data)
        except:
            #create the query object if not present already
            query_obj = Query.objects.create(query = query_)
            #get the articles for the query from api calls to reddit and newsapi
            articles_result = newssources.get_news(query_)
            #create the article objects for the query
            for article in articles_result:
                Article.objects.create(query = query_obj, headline = article['headline'], link = article['link'], source = article['source'])
            #get the articles for the query
            Article_list = Article.objects.filter(query = query_obj)
            #pass the articles to the serializer and return the response
            serializer = ArticleSerializer(Article_list, many = True)
            return Response(serializer.data)


def favourite(request, format = None):
    " Favourite/Unfavourite an article for a user or list all favourites for a user"
    #get the params for the request
    username = request.GET.get('user') or ''
    id = request.GET.get('pk') or ''
    #if no params are present, return error
    if username == '' or id == '':
        return JsonResponse("Please enter a valid url", safe = False)
    #if only username is present, return all favourites for the user
    elif username != "":
        try: #check if the user exists
            user_obj = User.objects.get(user = username)
        except: 
            #if the user does not exist, create the user
            user_obj = User.objects.create(user = username)
        #get the favourites for the user
        
        
        string =  username + "'s "  + 'list of favourited news will be listed here'
        return JsonResponse(string, safe = False)
    #if both username and id are present, then we will favourite/unfavourite the article
    else:
        string = username + "'s #" + str(id) + ' news has been favourited/unfavourited'
        return JsonResponse(string, safe = False)
