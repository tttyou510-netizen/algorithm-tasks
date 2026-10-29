# Algorithm Tasks & Mini Projects

This repository contains implementations, empirical benchmarks, and data structure simulations for CS314 Algorithm Analysis & Design mini-projects.

---

## Repository Structure

```text
algorithm-tasks/
├── task-1/                      # Mini Project: Empirical Analysis of Insertion Sort
│   ├── insertion_sort.py        # Insertion sort with comparison & shift counters
│   ├── experiment.py            # Benchmark script (n = 100 to 5,000) & graph plotting
│   ├── REPORT.md                # One-page report comparing with Merge Sort
│   ├── README.md                # Task 1 documentation
│   └── plots/                   # Generated empirical analysis charts
│
├── task-2/                      # Sorting Benchmark Lab
│   ├── sorting_algorithms.py    # Implementations: Insertion, Merge, Quick, Timsort
│   ├── benchmark.py             # Benchmark engine (n = 10^3 to 10^5) across data distributions
│   ├── README.md                # Task 2 documentation
│   └── plots/                   # Generated benchmark comparison curves
│
├── task-3/                      # OS Task Scheduler Simulation
│   ├── max_heap.py              # Array-based Binary Max-Heap (INSERT, EXTRACT-MAX, PEEK)
│   ├── task_scheduler.py        # Priority CPU Scheduler & tick simulation engine
│   ├── demo.py                  # Verification tests & simulated OS workload
│   └── README.md                # Task 3 documentation
│
├── requirements.txt             # Python project dependencies (matplotlib, numpy)
└── .gitignore                   # Virtual environment and cache ignores
```

---

## Getting Started

### 1. Setup Virtual Environment
```bash
python -m venv .venv

# On Windows (PowerShell):
.\.venv\Scripts\Activate.ps1

# Install requirements:
pip install -r requirements.txt
```

### 2. Run Any Task
- **Task 1: Insertion Sort Analysis**
  ```bash
  python task-1/insertion_sort.py
  python task-1/experiment.py
  ```

- **Task 2: Sorting Benchmark Lab**
  ```bash
  python task-2/benchmark.py
  ```

- **Task 3: OS Task Scheduler Simulation**
  ```bash
  python task-3/demo.py
  ```
