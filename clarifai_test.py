import unittest
import clarifai

class MyTest(unittest.TestCase):
	def test_url(self):
		cat = 'http://static.shop033.com//resources/18/160536/Image/white-cat-blue-eyes-640x360.jpg'
		d = clarifai.get_tags(cat)
		self.assertAlmostEqual(d['cute'], 0.0439758)

	def test_local(self):
		d = clarifai.get_tags_from_file('test.png')
		self.assertAlmostEqual(d['boy'], 0.0086441)

if __name__ == '__main__':	
	unittest.main()
