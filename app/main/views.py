from flask import render_template
from . import main
from ..requests import get_source


# app = Flask(__name__)

@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
  # Getting entertainment news
  entertainment_sources = get_source('entertainment')
  
  title = 'Home - Welcome to The best Movie Review Website Online'
  return render_template('index.html',entertainment = entertainment_sources)