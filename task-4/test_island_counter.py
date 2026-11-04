"""
Unit Tests for Task 4: Island Counter
"""

import unittest
import numpy as np
from island_counter import IslandCounter, count_islands


class TestIslandCounter(unittest.TestCase):

    def test_empty_grid(self):
        empty_grid = np.empty((0, 0), dtype=int)
        counter = IslandCounter(empty_grid)
        self.assertEqual(counter.count_islands_bfs(), 0)
        self.assertEqual(counter.count_islands_dfs(), 0)
        self.assertEqual(counter.max_area(), 0)

    def test_all_water(self):
        water = np.zeros((4, 4), dtype=int)
        counter = IslandCounter(water)
        self.assertEqual(counter.count_islands_bfs(), 0)
        self.assertEqual(counter.count_islands_dfs(), 0)
        self.assertEqual(counter.max_area(), 0)

    def test_all_land(self):
        land = np.ones((3, 3), dtype=int)
        counter = IslandCounter(land)
        self.assertEqual(counter.count_islands_bfs(), 1)
        self.assertEqual(counter.count_islands_dfs(), 1)
        self.assertEqual(counter.max_area(), 9)

    def test_single_cell_island(self):
        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        counter = IslandCounter(grid)
        self.assertEqual(counter.count_islands_bfs(), 1)
        self.assertEqual(counter.count_islands_dfs(), 1)
        self.assertEqual(counter.max_area(), 1)

    def test_standard_islands_4_connectivity(self):
        grid = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]
        ]
        counter = IslandCounter(grid)
        self.assertEqual(counter.count_islands_bfs(connectivity=4), 3)
        self.assertEqual(counter.count_islands_dfs(connectivity=4), 3)

        num_islands, labeled, sizes = counter.label_islands(connectivity=4)
        self.assertEqual(num_islands, 3)
        self.assertEqual(sizes[1], 4)
        self.assertEqual(sizes[2], 1)
        self.assertEqual(sizes[3], 2)
        self.assertEqual(counter.max_area(connectivity=4), 4)

    def test_diagonal_8_connectivity(self):
        grid = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
        counter = IslandCounter(grid)
        # In 4-connectivity, diagonals do not connect -> 5 separate islands
        self.assertEqual(counter.count_islands_bfs(connectivity=4), 5)
        self.assertEqual(counter.count_islands_dfs(connectivity=4), 5)

        # In 8-connectivity, all 5 connect into 1 large island
        self.assertEqual(counter.count_islands_bfs(connectivity=8), 1)
        self.assertEqual(counter.count_islands_dfs(connectivity=8), 1)
        self.assertEqual(counter.max_area(connectivity=8), 5)

    def test_dfs_recursive_and_iterative_consistency(self):
        rng = np.random.default_rng(999)
        grid = rng.choice([0, 1], size=(20, 20), p=[0.7, 0.3])
        counter = IslandCounter(grid)

        bfs_res = counter.count_islands_bfs()
        dfs_iter_res = counter.count_islands_dfs(iterative=True)
        dfs_rec_res = counter.count_islands_dfs(iterative=False)

        self.assertEqual(bfs_res, dfs_iter_res)
        self.assertEqual(bfs_res, dfs_rec_res)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            IslandCounter([1, 2, 3])  # 1D array

        with self.assertRaises(ValueError):
            IslandCounter([[0, 2], [1, 0]])  # Non-binary value 2


if __name__ == "__main__":
    unittest.main()
