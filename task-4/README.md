# Task 4: Island Counter (DFS & BFS Flood Fill)

## Overview
An algorithmic implementation of the **Island Counter** problem using **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** flood fill in Python and NumPy.

Given an $M \times N$ 2D grid representing a map of `1`s (land) and `0`s (water), an island is formed by connecting adjacent land cells horizontally or vertically (4-directional) or diagonally (8-directional).

### Key Features:
- **Graph Traversal & Flood Fill**:
  - **BFS Flood Fill**: Queue-based (`collections.deque`) exploration level-by-level.
  - **DFS Flood Fill**: Implemented both iteratively (using an explicit stack to prevent recursion overflow on large grids) and recursively.
- **Connected Component Analysis**:
  - **Labeling Matrix**: Marks each distinct island with a unique ID ($1, 2, \dots, K$).
  - **Island Statistics**: Computes areas, maximum island size, minimum size, and mean size.
- **Configurable Connectivity**:
  - 4-way connectivity (default: Up, Down, Left, Right).
  - 8-way connectivity (including diagonals).
- **NumPy Integration**:
  - Efficient boolean masking, matrix manipulation, and grid generation.

---

## Complexity Analysis

| Algorithm | Time Complexity | Space Complexity | Notes |
| :--- | :--- | :--- | :--- |
| **BFS (Queue)** | $\mathcal{O}(M \times N)$ | $\mathcal{O}(\min(M, N))$ | Explores expanding frontiers; optimal memory on square grids |
| **DFS (Iterative Stack)** | $\mathcal{O}(M \times N)$ | $\mathcal{O}(M \times N)$ | Avoids Python call-stack depth limits |
| **DFS (Recursive)** | $\mathcal{O}(M \times N)$ | $\mathcal{O}(M \times N)$ | Simple, bounded by Python `sys.setrecursionlimit` |

Every cell is examined and visited at most once, guaranteeing linear runtime proportional to total grid cells.

---

## File Structure
- `island_counter.py`: Core algorithm implementation, `IslandCounter` class, and executable simulation.

---

## How to Run

```bash
python island_counter.py
```

---

## Example Output

```text
--- Sample Grid ---
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1

Number of Islands (BFS): 3
Number of Islands (DFS): 3

--- Labeled Islands Grid ---
[[1 1 0 0 0]
 [1 1 0 0 0]
 [0 0 2 0 0]
 [0 0 0 3 3]]

Island Sizes: {1: 4, 2: 1, 3: 2}
Max Island Area: 4
```
