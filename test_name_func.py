import unittest
from name_func import get_formatted_name

class NamesTestCase(unittest.TestCase):
	''' to test name_func.py '''
	
	def test_first_last_name(self):
		''' handle names like Janis Joplin or not? '''
		formatted_name = get_formatted_name('Janis', 'Joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')
		
	def test_first_middle_last_name(self):
		''' handle names like Wolfgang Amedeus Mozart or not ? '''
		formatted_name = get_formatted_name('Wolfgang', 'mozart', 'amedeus')
		self.assertEqual(formatted_name, 'Wolfgang Amedeus Mozart')
		
unittest.main()

		