"""
Empirical Analysis Experiment for Insertion Sort.
Evaluates time, comparisons, and shifts for n = 100 to 5000 across:
  - Sorted inputs (Best Case: O(n))
  - Reverse-sorted inputs (Worst Case: O(n^2))
  - Random inputs (Average Case: O(n^2))
Also benchmarks Merge Sort for comparison.
"""

import time
import random
import os
from typing import List, Dict, Tuple
import matplotlib.pyplot as plt
import numpy as np

from insertion_sort import insertion_sort


def merge_sort(arr: List[int]) -> List[int]:
    """Standard merge sort for comparison."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


def run_experiment():
    sizes = [100, 250, 500, 1000, 1500, 2000, 3000, 4000, 5000]

    results = {
        "sorted": {"times": [], "comps": [], "shifts": []},
        "reverse": {"times": [], "comps": [], "shifts": []},
        "random": {"times": [], "comps": [], "shifts": []},
        "merge_sort_random": {"times": []},
    }

    print(f"{'n':>6} | {'Sorted (ms)':>12} | {'Reverse (ms)':>12} | {'Random (ms)':>12} | {'MergeSort (ms)':>14}")
    print("-" * 65)

    for n in sizes:
        # 1. Sorted array
        sorted_arr = list(range(n))
        t0 = time.perf_counter()
        _, c_sort, s_sort = insertion_sort(sorted_arr)
        t_sort = (time.perf_counter() - t0) * 1000.0

        # 2. Reverse array
        reverse_arr = list(range(n, 0, -1))
        t0 = time.perf_counter()
        _, c_rev, s_rev = insertion_sort(reverse_arr)
        t_rev = (time.perf_counter() - t0) * 1000.0

        # 3. Random array (average over 3 trials for stability)
        rand_times = []
        rand_comps = []
        rand_shifts = []
        for _ in range(3):
            rnd_arr = [random.randint(0, 100000) for _ in range(n)]
            t0 = time.perf_counter()
            _, c_rnd, s_rnd = insertion_sort(rnd_arr)
            t_rnd = (time.perf_counter() - t0) * 1000.0
            rand_times.append(t_rnd)
            rand_comps.append(c_rnd)
            rand_shifts.append(s_rnd)

        avg_rand_time = sum(rand_times) / len(rand_times)
        avg_rand_comps = sum(rand_comps) / len(rand_comps)
        avg_rand_shifts = sum(rand_shifts) / len(rand_shifts)

        # Merge sort on random array
        rnd_arr_ms = [random.randint(0, 100000) for _ in range(n)]
        t0 = time.perf_counter()
        _ = merge_sort(rnd_arr_ms)
        t_ms = (time.perf_counter() - t0) * 1000.0

        results["sorted"]["times"].append(t_sort)
        results["sorted"]["comps"].append(c_sort)
        results["sorted"]["shifts"].append(s_sort)

        results["reverse"]["times"].append(t_rev)
        results["reverse"]["comps"].append(c_rev)
        results["reverse"]["shifts"].append(s_rev)

        results["random"]["times"].append(avg_rand_time)
        results["random"]["comps"].append(avg_rand_comps)
        results["random"]["shifts"].append(avg_rand_shifts)

        results["merge_sort_random"]["times"].append(t_ms)

        print(f"{n:>6} | {t_sort:>12.3f} | {t_rev:>12.3f} | {avg_rand_time:>12.3f} | {t_ms:>14.3f}")

    plot_results(sizes, results)
    return sizes, results


def plot_results(sizes: List[int], results: Dict):
    os.makedirs("plots", exist_ok=True)
    n_arr = np.array(sizes)

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Plot 1: Empirical Running Times vs Input Size n
    ax1 = axes[0]
    ax1.plot(sizes, results["sorted"]["times"], 'o-', color='#2ca02c', label='Insertion Sort (Sorted) - Best O(n)')
    ax1.plot(sizes, results["random"]["times"], 's-', color='#1f77b4', label='Insertion Sort (Random) - Avg O(n²)')
    ax1.plot(sizes, results["reverse"]["times"], '^-', color='#d62728', label='Insertion Sort (Reverse) - Worst O(n²)')
    ax1.plot(sizes, results["merge_sort_random"]["times"], 'd--', color='#9467bd', label='Merge Sort (Random) - O(n log n)')

    # Normalized theoretical curves for reference
    scale_n2 = results["reverse"]["times"][-1] / (n_arr[-1] ** 2)
    scale_n = results["sorted"]["times"][-1] / n_arr[-1]
    ax1.plot(sizes, scale_n2 * (n_arr ** 2), ':', color='black', alpha=0.6, label='Theoretical O(n²)')
    ax1.plot(sizes, scale_n * n_arr, ':', color='gray', alpha=0.6, label='Theoretical O(n)')

    ax1.set_title("Running Time vs Input Size (n = 100 to 5000)", fontsize=13, fontweight='bold')
    ax1.set_xlabel("Input Size (n)", fontsize=11)
    ax1.set_ylabel("Execution Time (milliseconds)", fontsize=11)
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.legend(loc='upper left', fontsize=9)

    # Plot 2: Operations Count (Comparisons & Shifts)
    ax2 = axes[1]
    ax2.plot(sizes, results["random"]["comps"], 's-', color='#1f77b4', label='Random - Comparisons')
    ax2.plot(sizes, results["random"]["shifts"], 's--', color='#17becf', label='Random - Shifts')
    ax2.plot(sizes, results["reverse"]["comps"], '^-', color='#d62728', label='Reverse - Comparisons')
    ax2.plot(sizes, results["reverse"]["shifts"], '^--', color='#ff7f0e', label='Reverse - Shifts')
    ax2.plot(sizes, results["sorted"]["comps"], 'o-', color='#2ca02c', label='Sorted - Comparisons (n-1)')
    ax2.plot(sizes, results["sorted"]["shifts"], 'o--', color='#8c564b', label='Sorted - Shifts (0)')

    ax2.set_title("Comparisons & Shifts vs Input Size", fontsize=13, fontweight='bold')
    ax2.set_xlabel("Input Size (n)", fontsize=11)
    ax2.set_ylabel("Operation Count", fontsize=11)
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.legend(loc='upper left', fontsize=9)

    plt.tight_layout()
    output_path = os.path.join("plots", "empirical_analysis.png")
    plt.savefig(output_path, dpi=300)
    print(f"\n[+] Plot saved successfully to: {output_path}")


if __name__ == "__main__":
    run_experiment()
