
# Enhanced Pacman Game

This project is a customized version of the classic Pacman game. The primary objective is to navigate Pacman through a maze to collect all food pellets while ensuring that Pacman visits all four corners of the map. Unlike the original game, this version has **no ghosts**, allowing the focus to be on pathfinding and optimization.

## Features
- **No Ghosts**: Pacman can explore the maze without the threat of being chased.
- **Corner Visit Requirement**: Pacman must visit all four corners of the map at least once before completing the game.
- **Search Algorithms**: Three search algorithms are implemented to guide Pacman efficiently:
  - **Depth-First Search (DFS)**
  - **Uniform Cost Search (UCS)**
  - **A\* Search (A\*)**
  
## Heuristics for A*

The A* search algorithm uses a combination of the cost to reach the current state and a heuristic to estimate the remaining cost to the goal. The heuristic functions help A* prioritize which paths to explore by providing an estimate of the shortest possible path to the goal. In this game, two heuristics are implemented:

### 1. Minimum Euclidean Distance
This heuristic computes the **Euclidean distance** between the current position of Pacman and the nearest goal state (food pellet or corner of the maze). The Euclidean distance is the straight-line distance between two points in a 2D space, calculated as:

`distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)`

In this case, the heuristic calculates the minimum Euclidean distance to any of the goal positions (food pellets or corners), which helps guide Pacman towards the nearest goal.

### 2. Distance Between Two Farthest Food Pellets
This heuristic aims to find the **Manhattan distance** between the two farthest food pellets on the map and adds the minimum distance from Pacman's current position to one of these farthest pellets. The **Manhattan distance** is the sum of the absolute differences of their x and y coordinates:

`distance = |x1 - x2| + |y1 - y2|`

By focusing on the two farthest food pellets, this heuristic helps Pacman plan a path that efficiently covers the most distant areas of the map. The final heuristic value is the distance between the farthest two food pellets, plus the shorter distance from Pacman to one of them.

## Instructions

### Prerequisites
- Python 3.x installed on your system.
- Ensure all required Python files (e.g., `pacman.py`, `SearchAgents.py`) are in the same directory.

### How to Run

#### Depth-First Search (DFS)
```bash
python -B pacman.py -l smallMaze -p DfsFoodSearchAgent -z 0.5
python -B pacman.py -l mediumMaze -p DfsFoodSearchAgent -z 0.5
python -B pacman.py -l bigMaze -p DfsFoodSearchAgent -z 0.5
```

#### Uniform Cost Search (UCS)
```bash
python -B pacman.py -l smallMaze -p UcsFoodSearchAgent -z 0.5
python -B pacman.py -l mediumMaze -p UcsFoodSearchAgent -z 0.5
python -B pacman.py -l bigMaze -p UcsFoodSearchAgent -z 0.5
```

#### A* Search
```bash
python -B pacman.py -l smallMaze -p AStarFoodSearchAgent -z 0.5
python -B pacman.py -l mediumMaze -p AStarFoodSearchAgent -z 0.5
python -B pacman.py -l bigMaze -p AStarFoodSearchAgent -z 0.5
```

### Map Layouts
- **smallMaze**: A compact maze for quick testing.
- **mediumMaze**: A moderately challenging maze.
- **bigMaze**: A large maze for testing complex algorithms.

### Zoom Control
- Use the `-z` flag to control the zoom level of the game interface. A smaller value increases zoom.

## Algorithms Overview

### Depth-First Search (DFS)
- Explores as far as possible along each branch before backtracking.
- Simple but not guaranteed to find the shortest path.

### Uniform Cost Search (UCS)
- Expands the node with the least cost first.
- Guarantees the shortest path to complete the game.

### A* Search (A\*)
- Combines UCS with a heuristic to prioritize nodes closer to the goal.
- Efficient and guarantees the shortest path.

### Example Output
```bash
Path found with total cost of 802 in 0.5 seconds
Search nodes expanded: 2092
```
