import unittest
from app.models import Articles

class TestArticles(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''
    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_article = Articles('shhhh','ishhh','just testing','https://anylink.com')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
    
    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.author,'shhhh')
        self.assertEquals(self.new_article.title,'ishhhh')
        self.assertEquals(self.new_article.description,'just testing')
        self.assertEquals(self.new_article.url,'https://anylink.com')