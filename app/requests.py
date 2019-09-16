
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
    get_articles_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_details_url) as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(movie_details_data)

        article_object = None
        if articles_details_response:
            id = articles_details_response.get('id')
            title = articles_details_response.get('original_title')
            overview = articles_details_response.get('overview')
            poster = articles_details_response.get('poster_path')
            vote_average = articles_details_response.get('vote_average')
            vote_count = articles_details_response.get('vote_count')

            article_object = Article(id,title,overview,poster,vote_average,vote_count)

    return article_object
