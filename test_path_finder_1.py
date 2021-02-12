import unittest
from path_finder_1 import path_finder

maze_1 = "\n".join([
    ".W.",
    ".W.",
    "..."
])

maze_2 = "\n".join([
    ".W..",
    "....",
    ".w..",
    ".w..",
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

maze_5 = "\n".join([
    ".W...",
    ".W...",
    ".W.W.",
    "...W.",
    "...W.",
])

maze_6 = "\n".join([
    ".WWW..WW.W.........W..W.W....WW..W.......WW..W..W.",
    "....W..WW.W...W.WW....WWW...........WW..W.WW.....W",
    ".....W..W...W.......W..WW..W......W.........W.W..W",
    "W..W..W.W.W..W.W.W...W...W...W.......W....W....W..",
    ".W...W....W.W...WWW.WWW..W....W..W...WW......W...W",
    "W.........W..W.......W..............W....WWW.W....",
    "....W......W...WW........WWW...W.W.WW..W.......W..",
    ".W..W....W............W.W..WWWW.WW..WWW...WW......",
    "......WWW........WW..W...WWW.WW...........WW.W..WW",
    ".WW......W....W...WWW...........W.....W...W....W.W",
    "....WW...........W.........W...W..................",
    ".W..W....W......W...W.W.......WW...W..............",
    "WWW........WW..W...W...WW.W..WW...WW.WWW...W.WWW..",
    "...W...........W..W.W.W..W..W.W.WW..W.W...........",
    "...........WW..W.WW.....W.....W........W.W..W.W...",
    ".W..W.W..................W...W.........WWWW....W..",
    "....W....W........W........W.W...W.W..W.W....WW...",
    ".W.......W......W.......W.....W....W.W.....WW.....",
    "WW.....W...W........W.W........WWWWW....W.W..W.W..",
    "...WWWW........W.WW.........W........W.W.....W.W.W",
    ".W..W..W....W.W........W........W.........W.......",
    "WW..WW......W....W....W.W...........W.....W.......",
    "..W..W...WWW...W.W.........W..W..W...WW.W.......W.",
    "WW.W.......WW..WW.W..W....WW............W....W....",
    "W.W...W.WW..WW.W....WW........WWW....WWW.W....W...",
    ".......W....W.....W.W.W..W.W.........W.....W....W.",
    "..WW...W.........WW....WW......W....W.......W.WWW.",
    "WW.WW..W.W.WW....WW.W..WW......W.W..........W.W...",
    "W..W.........W..W.........W....W......W......W....",
    "....W..WW.W...W.W.W....W.......W.W...W..WW....WW..",
    "......WW.........W....WW....W..W..WWW.W....W..WW..",
    "W.....W.W..WWW.W...WW....W...W.........WW..W....W.",
    "............W...W....W...W........W....WW...W.W...",
    "............W...W.....W...W..W.W....W..WWWW......W",
    "..W..W...W..............W.W...W......W...W.......W",
    "....W.W...W..W..W...W..W....W.W...........W..W.W.W",
    ".............W...W....W....W.....W..W.......W.....",
    "...WW.W..W....W....W........W.WWW..........W....WW",
    "....WW..W................W..W..W.WW.WW..W....WW..W",
    ".....W.W......W..WW...W..WW...W.....W.W.....WW.W..",
    "WW..WW.W....WW....W..W...W...WW....W.WW....W......",
    "W..........W..WWWW..W..WW.WWW..W.....W..W...W...W.",
    "..W................WW..WW.....W.......WW..WW...W..",
    "W..W..W....W...WW.W......WWW.W.WWW.....WW...W..W.W",
    ".W...W.W.WWW...W.......WW........WW...W.W...W...WW",
    "W..W.....W...W...W......W.WW...W..W..........W....",
    "........W...W..WWW.WW.W.WW........W..W....WWW.W..W",
    ".......W.WW..W........W..W....W....W.W..WW........",
    "..W.........WWWW...WW...W.W.W.W.WW..W....W..W.W...",
    ".....W.....W.....W.W.W.....WW...........WWWW...WW.",
])


class Test(unittest.TestCase):
    def test_maze_1(self):
        self.assertEqual(path_finder(maze_1), True)

    def test_maze_2(self):
        self.assertEqual(path_finder(maze_2), True)

    def test_maze_3(self):
        self.assertEqual(path_finder(maze_3), True)

    def test_maze_4(self):
        self.assertEqual(path_finder(maze_4), False)

    def test_maze_5(self):
        self.assertEqual(path_finder(maze_5), True)

    def test_maze_6(self):
        self.assertEqual(path_finder(maze_6), True)


if __name__ == '__main__':
    unittest.main()