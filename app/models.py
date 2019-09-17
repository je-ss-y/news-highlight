class Source:
    '''
    Movie class to define news Objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


class Articles:
    '''
    Sources class that defines source objects
    '''
    def __init__(self,id,author,title,description,content,url,publishedAt):
        '''
        Function that initiates the sources class
        '''
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.content = content
        self.url = url
       
