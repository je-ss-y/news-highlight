from flask import render_template
from . import main
from ..requests import get_source , get_articles



# app = Flask(__name__)

@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
  # Getting entertainment news
  entertainment_sources = get_source('entertainment')
  print(entertainment_sources)
  
   # Getting entertainment news
  business_sources = get_source('business')
  
  return render_template('index.html',entertainment = entertainment_sources, business = business_sources)

@main.route('/article/<id>')

def articles(id):

  '''
  View article page function that returns the news details page and its data
  '''
  articles = get_articles(id)
  # title = f'{articles.title}'

  return render_template('articles.html',articles = articles)