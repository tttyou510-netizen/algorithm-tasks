# Empirical Analysis of Insertion Sort — Report

## 1. Overview
This experiment analyzes the empirical runtime and internal operation counts (comparisons and shifts) of the **Insertion Sort** algorithm across three input configurations:
- **Sorted array** (Best case)
- **Reverse-sorted array** (Worst case)
- **Random array** (Average case)

Input sizes evaluated range from $n = 100$ to $n = 5{,}000$.

---

## 2. Theoretical vs. Empirical Complexity

| Input Case | Comparisons (Theoretical) | Shifts (Theoretical) | Time Complexity | Observed Curve Match |
| :--- | :--- | :--- | :--- | :--- |
| **Best (Sorted)** | $n - 1$ | $0$ | $\Theta(n)$ | Linear growth |
| **Worst (Reverse)** | $\frac{n(n-1)}{2}$ | $\frac{n(n-1)}{2}$ | $\Theta(n^2)$ | Exact quadratic parabola |
| **Average (Random)** | $\approx \frac{n(n-1)}{4}$ | $\approx \frac{n(n-1)}{4}$ | $\Theta(n^2)$ | Quadratic parabola ($\approx \frac{1}{2}$ worst case) |

### Key Observations:
1. **Sorted Data ($\mathcal{O}(n)$)**: Each new element is compared once with its predecessor and immediately placed. Zero shifts occur. Running time remains practically negligible (< 1 ms even at $n = 5{,}000$).
2. **Reverse-Sorted Data ($\mathcal{O}(n^2)$)**: Every element must shift all preceding elements. At $n = 5{,}000$, total comparisons and shifts reach $\approx 1.25 \times 10^7$ operations each, matching the upper-bound quadratic curve.
3. **Random Data ($\mathcal{O}(n^2)$)**: Elements shift halfway on average. Both comparison and shift counts closely track $\approx \frac{n^2}{4}$.

---

## 3. Comparison with Merge Sort

| Metric | Insertion Sort | Merge Sort |
| :--- | :--- | :--- |
| **Best Case Time** | $\mathcal{O}(n)$ | $\mathcal{O}(n \log n)$ |
| **Average Case Time** | $\mathcal{O}(n^2)$ | $\mathcal{O}(n \log n)$ |
| **Worst Case Time** | $\mathcal{O}(n^2)$ | $\mathcal{O}(n \log n)$ |
| **Auxiliary Space** | $\mathcal{O}(1)$ (In-place) | $\mathcal{O}(n)$ |
| **Stability** | Stable | Stable |
| **Small Array Overhead** | Extremely low overhead (fast for $n < 50$) | High recursive/merge allocation overhead |

### Conclusion:
- For small datasets or nearly-sorted data, Insertion Sort is superior due to minimal overhead and adaptive linear runtime $\mathcal{O}(n)$.
- As $n$ grows past $1{,}000$, Merge Sort drastically outperforms Insertion Sort because $\mathcal{O}(n \log n)$ diverges sharply from $\mathcal{O}(n^2)$.
