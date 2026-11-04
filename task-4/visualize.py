"""
Task 4: Visualization and Benchmarking for Island Counter
Generates plots showing the original grid, colored island clusters, and BFS vs DFS performance.
"""

import os
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from island_counter import IslandCounter


def generate_random_grid(rows: int, cols: int, land_prob: float = 0.35, seed: int = 42) -> np.ndarray:
    """Generate a reproducible random 2D binary grid."""
    rng = np.random.default_rng(seed)
    return rng.choice([0, 1], size=(rows, cols), p=[1.0 - land_prob, land_prob])


def plot_islands(grid: np.ndarray, save_path: str):
    """Plot original binary grid, labeled components, and island size distribution."""
    counter = IslandCounter(grid)
    num_islands, labeled_grid, sizes = counter.label_islands(method="bfs", connectivity=4)
    areas = list(sizes.values())

    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

    # 1. Binary Grid (Water vs Land)
    cmap_binary = colors.ListedColormap(["#2b5c8f", "#48a868"])  # Deep Blue (Water), Green (Land)
    im0 = axes[0].imshow(grid, cmap=cmap_binary, interpolation="nearest")
    axes[0].set_title(f"Original Binary Grid ({grid.shape[0]}x{grid.shape[1]})\n0 = Water, 1 = Land", fontsize=12, fontweight="bold")
    cbar0 = plt.colorbar(im0, ax=axes[0], ticks=[0, 1], fraction=0.046, pad=0.04)
    cbar0.ax.set_yticklabels(["Water (0)", "Land (1)"])
    axes[0].set_xlabel("Column Index")
    axes[0].set_ylabel("Row Index")

    # 2. Labeled Islands with Distinct Colors
    if num_islands > 0:
        base_cmap = plt.colormaps["turbo"].resampled(num_islands + 1)
        cmap_list = [base_cmap(i) for i in range(num_islands + 1)]
        cmap_list[0] = (0.17, 0.36, 0.56, 1.0)  # Water is blue
        custom_cmap = colors.ListedColormap(cmap_list)
        bounds = np.arange(-0.5, num_islands + 1.5, 1)
        norm = colors.BoundaryNorm(bounds, custom_cmap.N)

        im1 = axes[1].imshow(labeled_grid, cmap=custom_cmap, norm=norm, interpolation="nearest")
        axes[1].set_title(f"Flood Fill Labeled Islands\nTotal Found: {num_islands} Islands", fontsize=12, fontweight="bold")
        cbar1 = plt.colorbar(im1, ax=axes[1], fraction=0.046, pad=0.04)
        cbar1.set_label("Island ID")
    else:
        axes[1].imshow(labeled_grid, cmap="Blues", interpolation="nearest")
        axes[1].set_title("No Islands Found (All Water)", fontsize=12, fontweight="bold")

    axes[1].set_xlabel("Column Index")
    axes[1].set_ylabel("Row Index")

    # 3. Island Area Distribution
    if areas:
        axes[2].hist(areas, bins=max(10, min(30, len(areas))), color="#e67e22", edgecolor="black", alpha=0.85)
        axes[2].set_title(f"Island Size Distribution\nMax Area: {max(areas)} | Mean Area: {np.mean(areas):.1f}", fontsize=12, fontweight="bold")
        axes[2].set_xlabel("Island Area (Number of Cells)")
        axes[2].set_ylabel("Count")
        axes[2].grid(True, linestyle="--", alpha=0.5)
    else:
        axes[2].text(0.5, 0.5, "No Islands", horizontalalignment="center", verticalalignment="center", transform=axes[2].transAxes)
        axes[2].set_title("Island Size Distribution", fontsize=12, fontweight="bold")

    plt.tight_layout()
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[OK] Saved island visualization to: {save_path}")


def run_benchmark(save_path: str):
    """Benchmark BFS vs DFS across increasing grid sizes."""
    sizes = [20, 50, 100, 150, 200, 300, 400]
    bfs_times = []
    dfs_times = []

    print("\n--- Running BFS vs DFS Performance Benchmark ---")
    print(f"{'Grid Size':<12} | {'Cells':<10} | {'BFS Time (s)':<15} | {'DFS Time (s)':<15} | {'Islands':<8}")
    print("-" * 70)

    for n in sizes:
        grid = generate_random_grid(n, n, land_prob=0.35, seed=n)
        counter = IslandCounter(grid)

        # BFS benchmark
        t0 = time.perf_counter()
        count_bfs = counter.count_islands_bfs()
        t_bfs = time.perf_counter() - t0

        # DFS benchmark (iterative)
        t0 = time.perf_counter()
        count_dfs = counter.count_islands_dfs(iterative=True)
        t_dfs = time.perf_counter() - t0

        assert count_bfs == count_dfs, f"Mismatch at size {n}: BFS {count_bfs} != DFS {count_dfs}"

        bfs_times.append(t_bfs)
        dfs_times.append(t_dfs)

        print(f"{f'{n}x{n}':<12} | {n*n:<10} | {t_bfs:<15.5f} | {t_dfs:<15.5f} | {count_bfs:<8}")

    # Plot Benchmark
    plt.figure(figsize=(9, 5.5))
    total_cells = [n * n for n in sizes]
    plt.plot(total_cells, bfs_times, marker="o", linewidth=2, color="#2980b9", label="BFS Flood Fill (Queue)")
    plt.plot(total_cells, dfs_times, marker="s", linewidth=2, linestyle="--", color="#c0392b", label="DFS Flood Fill (Stack)")

    plt.title("BFS vs DFS Flood Fill Runtime Complexity O(M * N)", fontsize=13, fontweight="bold")
    plt.xlabel("Total Grid Cells (M × N)", fontsize=11)
    plt.ylabel("Execution Time (seconds)", fontsize=11)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=11)
    plt.tight_layout()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[OK] Saved benchmark plot to: {save_path}")


if __name__ == "__main__":
    plots_dir = os.path.join(os.path.dirname(__file__), "plots")
    
    # 1. Visualize a 30x40 island grid
    grid = generate_random_grid(30, 40, land_prob=0.38, seed=123)
    plot_islands(grid, os.path.join(plots_dir, "islands_visualization.png"))

    # 2. Benchmark runtime scaling
    run_benchmark(os.path.join(plots_dir, "flood_fill_benchmark.png"))
