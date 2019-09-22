# import unittest
# from models import source
# Source = source.Source

# class SourceTest(unittest.TestCase):
#     '''
#     Test Class to test the behaviour of the Source class
#     '''

#     def setUp(self):
#         '''
#         Set up method that will run before every Test
#         '''
#         self.new_source = Source(1789,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs','entertainment','rwanda')

#     def test_instance(self):
#         self.assertTrue(isinstance(self.new_source,Source))

#     def test_to_check_instance_variables(self):
#         '''
#         Test function to check instance variables
#         '''
#         self.assertEquals(self.new_source.id,'1789')
#         self.assertEquals(self.new_source.name,'Python Must Be Crazy')
#         self.assertEquals(self.new_source.description,'A thrilling new Python Series')
#         self.assertEquals(self.new_source.url,'https://image.tmdb.org/t/p/w500/khsjha27hbs')
#         self.assertEquals(self.new_source.category,'general')
#         self.assertEquals(self.new_source.country,'rwanda')

# if __name__ == '__main__':
#     unittest.main()
