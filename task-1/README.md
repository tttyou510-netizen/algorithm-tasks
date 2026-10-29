# Task 1: Empirical Analysis of Insertion Sort

## Overview
This task covers:
1. **Implementation**: `insertion_sort` in Python with real-time counting of **comparisons** and **shifts**.
2. **Experimentation**: Empirical benchmarks across input sizes $n = 100$ to $5{,}000$ on:
   - Sorted inputs ($\mathcal{O}(n)$ best case)
   - Reverse-sorted inputs ($\mathcal{O}(n^2)$ worst case)
   - Random inputs ($\mathcal{O}(n^2)$ average case)
3. **Analysis**: Plotting running times against theoretical $\mathcal{O}(n)$ and $\mathcal{O}(n^2)$ curves.
4. **Report**: Detailed comparison with Merge Sort ($\mathcal{O}(n \log n)$).

## Project Structure
- `insertion_sort.py`: The core algorithm function `insertion_sort(arr)` returning `(sorted_arr, comparisons, shifts)`.
- `experiment.py`: Runs benchmarks, logs results, and generates graphs into `plots/`.
- `REPORT.md`: Findings summary and Merge Sort comparison.

## How to Run
```bash
# 1. Run basic demo
python insertion_sort.py

# 2. Run full experiment & generate plots
python experiment.py
```
