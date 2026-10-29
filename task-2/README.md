# Task 2: Sorting Benchmark Lab

## Overview
A comprehensive benchmark comparing four sorting algorithms across multiple dataset configurations:
- **Algorithms**:
  1. `Insertion Sort` ($\mathcal{O}(n^2)$)
  2. `Merge Sort` ($\mathcal{O}(n \log n)$)
  3. `Quick Sort` (Randomized pivot to prevent $\mathcal{O}(n^2)$ degeneration)
  4. `Python sorted()` (Timsort, C-level implementation)
- **Data Configurations**:
  - Random data
  - Pre-sorted data
  - Reverse-sorted data
- **Input Sizes**:
  - $n = 10^3$ to $10^5$ ($1{,}000$ to $100{,}000$)
- **Tools**:
  - Python, `time.perf_counter`, `matplotlib`

## File Structure
- `sorting_algorithms.py`: Full implementations of insertion sort, merge sort, randomized quick sort, and Timsort wrapper.
- `benchmark.py`: Runs execution time measurements, formats terminal tables, and generates log-log comparison charts saved to `plots/`.

## Running the Benchmark
```bash
python benchmark.py
```
