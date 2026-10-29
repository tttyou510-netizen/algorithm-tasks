import time
import random
import matplotlib.pyplot as plt


# 1. Insertion Sort
def insertion_sort(arr):
    a = list(arr)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# 2. Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
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


# 3. Quick Sort (using middle pivot to handle sorted/reversed data)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# 4. Benchmark Function
def benchmark():
    sizes = [1000, 2000, 5000, 10000]  # n from 10^3 upwards
    
    times_insertion = []
    times_merge = []
    times_quick = []
    times_builtin = []
    
    print(f"{'n':>6} | {'Insertion':>10} | {'Merge':>10} | {'Quick':>10} | {'sorted()':>10}")
    print("-" * 55)

    for n in sizes:
        # Testing on random data
        data = [random.randint(0, 100000) for _ in range(n)]

        # Insertion sort
        t0 = time.perf_counter()
        insertion_sort(data)
        t_ins = time.perf_counter() - t0

        # Merge sort
        t0 = time.perf_counter()
        merge_sort(data)
        t_merge = time.perf_counter() - t0

        # Quick sort
        t0 = time.perf_counter()
        quick_sort(data)
        t_quick = time.perf_counter() - t0

        # Python sorted()
        t0 = time.perf_counter()
        sorted(data)
        t_builtin = time.perf_counter() - t0

        times_insertion.append(t_ins)
        times_merge.append(t_merge)
        times_quick.append(t_quick)
        times_builtin.append(t_builtin)

        print(f"{n:>6} | {t_ins:>9.4f}s | {t_merge:>9.4f}s | {t_quick:>9.4f}s | {t_builtin:>9.4f}s")

    # Plot the results
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, times_insertion, label="Insertion Sort")
    plt.plot(sizes, times_merge, label="Merge Sort")
    plt.plot(sizes, times_quick, label="Quick Sort")
    plt.plot(sizes, times_builtin, label="Python sorted()")

    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithms Benchmark")
    plt.legend()
    plt.grid(True)
    plt.savefig("benchmark_plot.png")
    print("\nSaved benchmark plot to benchmark_plot.png")


if __name__ == "__main__":
    benchmark()
