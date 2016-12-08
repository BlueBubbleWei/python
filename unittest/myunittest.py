import unittest
def division_function(x,y):
 	return round(float(x)/y, 6)



class TestDivision(unittest.TestCase):
 	def test_int(self):
 		self.assertEqual(division_function(9,3),3)


 	def test_int2(self):
 		self.assertEqual(division_function(9,4),2.25)


 	def test_float(self):
 		self.assertEqual(division_function(4.2,3),1.4)


if __name__=='__main__':
	unittest.main()


 		