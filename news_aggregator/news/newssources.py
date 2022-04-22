from newsapi import NewsApiClient
import praw
import json

def getnews_newsapi(q):
    newsapi = NewsApiClient(api_key='f69c3e9493764e2883bf29ab91eadade')
    news = newsapi.get_top_headlines(q=q, category='general')
    results = []
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
        results.append(json.dump(result))
    return results

def getnews_reddit(q):
    reddit = praw.Reddit(client_id='Hflyqrr1LnU2A-p8XJ7Zew',
                         client_secret='O8ejEXRojls-xQY_Bb3wABaRCiGBaw',
                         user_agent='reddit Bot')
    subreddit = reddit.subreddit('news')
    if q == "":
        top_subreddit = subreddit.new(limit=20)
    else:
        top_subreddit = subreddit.search(q, limit=20)
    results = []
    for submission in top_subreddit:
        result = {
            'headline' : submission.title,
            'link' : submission.url,
            'source' : 'reddit',
        }
        results.append(json.dump(result))
    return results             

def get_news(q = ""):
    reddit_results = getnews_reddit(q)
    newsapi_results = getnews_newsapi(q)
    results = reddit_results + newsapi_results
    return results