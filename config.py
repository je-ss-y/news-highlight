import os

class Config:

    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_API_KEY ='7c12e4075c294da0b2ce606c9cf24e7a'
    ARTICLES_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin&apiKey=7c12e4075c294da0b2ce606c9cf24e7a'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}