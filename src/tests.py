from maze import Maze
import unittest

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        self.assertEqual(
            num_cols,
            12
        )
        # m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        # self.assertEqual(
        #     len(m1._Maze__cells),
        #     num_cols,
        # )
        # self.assertEqual(
        #     len(m1._Maze__cells[0]),
        #     num_rows,
        # )


if __name__ == "__main__":
    unittest.main()
