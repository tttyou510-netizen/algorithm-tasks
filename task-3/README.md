# Task 3: OS Task Scheduler Simulation

## Overview
Simulates an Operating System priority CPU scheduler using a custom binary **Max-Heap** priority queue.
Implements:
- **Max-Heap Core Operations**:
  - `INSERT`: Adds a task in $\mathcal{O}(\log n)$ time.
  - `EXTRACT-MAX`: Removes and dispatches the highest-priority task in $\mathcal{O}(\log n)$ time.
  - `PEEK-MAX`: Inspects the root task in $\mathcal{O}(1)$ time.
- **Task Modeling**:
  - `Task`: encapsulates Task ID, name, priority level, burst time, arrival time, and remaining execution time.
- **Scheduler Simulation**:
  - Models clock cycles, ready queue arrivals, task dispatching, context execution, waiting time, and turnaround time metrics.

## File Structure
- `max_heap.py`: Array-backed Binary Max-Heap implementation with sift-up and sift-down.
- `task_scheduler.py`: CPU Scheduler simulator with timeline logging and performance metrics.
- `demo.py`: Test runner demonstrating heap correctness and a mixed real-time OS workload.

## How to Run
```bash
python demo.py
```
