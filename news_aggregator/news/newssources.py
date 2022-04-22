from newsapi import NewsApiClient
import praw
import json

def getnews_newsapi(q):
    "Get news from newsapi"
    newsapi = NewsApiClient(api_key='f69c3e9493764e2883bf29ab91eadade') #api key
    news = newsapi.get_top_headlines(q=q, category='general') #top headlines from category general
    results = []
    i = 0
    for article in news['articles']:
        source_name = article['source']['name']
        length = len(source_name)+3
        title = article['title']
        actualTitle = title[:len(title)-length]
        url = article['url']
        source = 'newsapi'
        result = {
            'headline': actualTitle,
            'link' : url,
            'source' : source,
        }
        results.append(result)
        i += 1
        if i == 5:
            break
    return results

def getnews_reddit(q):
    "Get news from reddit"
    reddit = praw.Reddit(client_id='Hflyqrr1LnU2A-p8XJ7Zew', #client id
                         client_secret='O8ejEXRojls-xQY_Bb3wABaRCiGBaw', #client secret
                         user_agent='reddit Bot') #arbitrary user agent
    #get posts from /r/news subreddit
    subreddit = reddit.subreddit('news')
    #if no query is present, get new posts from the subreddit
    if q == "":
        top_subreddit = subreddit.new(limit=5)
    #if query is present, get posts from the subreddit that match the query
    else:
        top_subreddit = subreddit.search(q, limit=5)
    #get the title and url of the posts
    results = []
    for submission in top_subreddit:
        result = {
            'headline' : submission.title,
            'link' : submission.url,
            'source' : 'reddit',
        }
        results.append(result)
    return results             

def get_news(q = ""):
    "Get news from newsapi and reddit"
    reddit_results = getnews_reddit(q)
    newsapi_results = getnews_newsapi(q)
    results = reddit_results + newsapi_results
    return results