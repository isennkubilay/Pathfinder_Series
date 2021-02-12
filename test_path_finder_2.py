import unittest
from path_finder_2 import path_finder





maze_1 = "\n".join([
  ".W.",
  ".W.",
  "..."
])

maze_2 = "\n".join([
  ".W.",
  ".W.",
  "W.."
])

maze_3 = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])

maze_4 = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])

class Test(unittest.TestCase):
    def test_maze_1(self):
        self.assertEqual(path_finder(maze_1), 4)
    
    def test_maze_2(self):
        self.assertEqual(path_finder(maze_2), False)
    
    def test_maze_3(self):
        self.assertEqual(path_finder(maze_3), 10)
    
    def test_maze_4(self):
        self.assertEqual(path_finder(maze_4), False)


if __name__ == "__main__":
    unittest.main