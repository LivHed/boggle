import unittest
import boggle
from string import ascii_uppercase

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
   
   def test_grid_size_width_times_height(self):
       """
        Test is to ensure that the total size of the grid
        is equal to width * height
        """
       grid = boggle.make_grid(2, 3)
       self.assertEqual(len(grid), 6)
       
   def test_grid_coordinates(self):
       """
       Test to ensure that all of the coordinates 
       inside of the grid can be accessed.
       """
       grid = boggle.make_grid(2, 2)
       self.assertIn((0, 0), grid)
       self.assertIn((0, 1), grid)
       self.assertIn((1, 0), grid)
       self.assertIn((1, 1), grid)
       self.assertNotIn((2, 2), grid)
       
   def test_grid_is_filled_with_letters(self):
        """
        Ensure that each of the coordinates in the grid
        contains letters
        """
        grid = boggle.make_grid(2, 3)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
            