import unittest
import boggle

class TestBoggle(unittest.TestCase):
   """
   The test suite for boggle solver
   """
   
   def test_can_create_an_empty_grid(self):
       """
       Test to see if I can create an empty grid
       """
       grid = boggle.make_grid(0, 0) #we pass two arguments height and width.The simplest grid is one with no rows or columns so 0 0 is used.
       self.assertEqual(len(grid), 0)
   