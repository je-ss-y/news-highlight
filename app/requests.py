
import urllib.request,json
from .models import Source



# Getting api key
api_key = None


# Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)
    return source_results

def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name= source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        # if poster:
        source_object = Source(id,name,description,url,category,language,country)
        source_results.append(source_object)

    
    return source_results

def get_articles(id):
    '''
    Function that gets articles based on the source id
    '''
    get_articles_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
    
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None
        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)
        
    return articles_results

def process_articles(articles_list):
    '''
    Function that processes the json results for the articles
    '''
    articles_results = []
    
    for article in articles_list:
         id = article.get('id')

         author = article.get('author')
         title = article.get('title')
         description = article.get('description')
         content = article.get('content')
         url = article.get('url')
        
         if urlToImage:
            articles_result = Articles(id,author,title,description,content,url)
            articles_results.append(articles_result)
    return articles_results



