# GoIT Algorithm Fundamentals Project

A collection of algorithm implementations and data structures for learning and practice.

## 📋 Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Tasks](#tasks)
  - [Task 1: Linked List](#task-1-linked-list)
  - [Task 2: Pythagorean Tree](#task-2-pythagorean-tree)
  - [Task 3: Dijkstra's Algorithm](#task-3-dijkstras-algorithm)
  - [Task 4 & 5: Heap to Tree & Tree Traversal](#task-4--5-heap-to-tree--tree-traversal)
  - [Task 6: Knapsack Problem](#task-6-knapsack-problem)
  - [Task 7: Monte Carlo Simulation](#task-7-monte-carlo-simulation)
- [Usage](#usage)
- [Requirements](#requirements)

## Installation

This project uses `uv` for dependency management. To install dependencies:

```bash
uv sync
```

## Project Structure

```
goit-algo-fp/
├── src/
│   └── goit_algo_fp/
│       ├── task_1/          # Linked List implementation
│       ├── task_2/          # Pythagorean Tree visualization
│       ├── task_3/           # Dijkstra's algorithm
│       ├── task_4_5/         # Heap to Tree & Tree Traversal (Task 4 & 5 combined)
│       ├── task_6/           # Knapsack problem algorithms
│       ├── task_7/           # Monte Carlo simulation
│       └── core/             # Core utilities and helpers
├── pyproject.toml
└── README.md
```

## Tasks

### Task 1: Linked List

Implementation of a singly linked list with operations:
- **Reverse**: Reverse the linked list in-place
- **Sort**: Sort the linked list using merge sort
- **Merge Sorted Lists**: Merge two sorted linked lists into one

**Run:**
```bash
uv run python -m goit_algo_fp.task_1
```

### Task 2: Pythagorean Tree

Fractal tree visualization using the Pythagorean theorem. Creates a recursive tree structure using turtle graphics.

**Run:**
```bash
uv run python -m goit_algo_fp.task_2
```

**Parameters:**
- `length`: Initial branch length
- `depth`: Recursion depth
- `angle`: Branch angle in degrees
- `ratio`: Length reduction ratio for child branches

### Task 3: Dijkstra's Algorithm

Shortest path algorithm implementation using binary heap. Finds the shortest paths from a starting vertex to all other vertices in a weighted graph.

**Run:**
```bash
uv run python -m goit_algo_fp.task_3
```

**Usage:**
```python
from goit_algo_fp.task_3.graph import Graph
from goit_algo_fp.task_3.dijkstra import dijkstra, reconstruct_path

# Build graph
graph = Graph()
graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 1)
graph.add_edge("C", "B", 2)

# Find shortest paths
distances, previous = dijkstra(graph, "A")

# Reconstruct path
path = reconstruct_path(previous, "A", "B")
```

### Task 4 & 5: Heap to Tree & Tree Traversal

Combined implementation of Task 4 and Task 5 in a single file:
- **Task 4**: Converts a heap (list representation) to a binary tree structure
- **Task 5**: Implements BFS (Breadth-First Search) and DFS (Depth-First Search) tree traversal algorithms with visualization

**Run:**
```bash
uv run python -m goit_algo_fp.task_4_5
```

**Features:**
- Converts Python's `heapq` heap list to a binary tree structure
- Visualizes tree traversals using BFS and DFS algorithms
- Generates graph visualizations showing traversal order with color-coded nodes

**Usage:**
```python
import heapq
from goit_algo_fp.core.adapters.heap_to_tree import heap_to_tree

# Create a heap
heap = [0, 4, 5, 10, 1, 3, 7, 2, 6, 8, 9]
heapq.heapify(heap)

# Convert to tree
tree = heap_to_tree(heap)
```

### Task 6: Knapsack Problem

Two algorithms for solving the 0/1 knapsack problem:
- **Dynamic Programming**: Optimal solution using DP
- **Greedy Algorithm**: Fast approximation using calories-to-cost ratio

Maximizes calories within a given budget constraint.

**Run:**
```bash
uv run python -m goit_algo_fp.task_6
```

**Usage:**
```python
from goit_algo_fp.task_6.algorithms import dynamic_programming, greedy_algorithm

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
}

budget = 100

# Optimal solution
dp_result = dynamic_programming(items, budget)

# Greedy approximation
greedy_result = greedy_algorithm(items, budget)
```

### Task 7: Monte Carlo Simulation

Monte Carlo simulation for dice rolls. Simulates a large number of dice throws and calculates probabilities for each possible sum.

**Run:**
```bash
uv run python -m goit_algo_fp.task_7
```

**Features:**
- Simulates two 6-sided dice
- Calculates probabilities for sums 2-12
- Compares Monte Carlo results with theoretical probabilities
- Generates probability table and bar chart visualization

**Usage:**
```python
from goit_algo_fp.task_7 import (
    monte_carlo_simulation,
    get_theoretical_probabilities,
    print_probability_table,
    plot_probabilities,
)

# Run simulation
probabilities = monte_carlo_simulation(100000)

# Get theoretical probabilities
theoretical = get_theoretical_probabilities()

# Display results
print_probability_table(probabilities, theoretical)
plot_probabilities(probabilities, theoretical)
```

For detailed conclusions and analysis comparing Monte Carlo results with theoretical calculations, see the [Task 7 README](src/goit_algo_fp/task_7/README.md).

## Usage

Each task can be run independently:

```bash
# Task 1: Linked List
uv run python -m goit_algo_fp.task_1

# Task 2: Pythagorean Tree
uv run python -m goit_algo_fp.task_2

# Task 3: Dijkstra's Algorithm
uv run python -m goit_algo_fp.task_3

# Task 4 & 5: Heap to Tree & Tree Traversal
uv run python -m goit_algo_fp.task_4_5

# Task 6: Knapsack Problem
uv run python -m goit_algo_fp.task_6

# Task 7: Monte Carlo Simulation
uv run python -m goit_algo_fp.task_7
```

## Requirements

- Python >= 3.11
- uv (package manager)

### Dependencies

- `black>=25.12.0` - Code formatter
- `matplotlib>=3.10.8` - Plotting and visualization
- `networkx>=3.6.1` - Graph algorithms
- `numpy>=2.4.0` - Numerical computing
- `ruff>=0.14.10` - Linter

## Author

Yaroslav Zahoruiko (yaroslav.zahoruiko@cd.p2h.com)

