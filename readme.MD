# Search Algorithms and State Representations

This repository contains a collection of Python classes and functions that implement various search algorithms and state representations for solving problems in different domains. These algorithms are commonly used in artificial intelligence and computer science to explore state spaces and find solutions to complex problems.

## Contents

- [Search Algorithms](#search-algorithms)
- [State Classes](#state-classes)
- [Heuristic Functions](#heuristic-functions)
- [Test Cases](#test-cases)
- [What I Learned](#what-i-learned)

## Search Algorithms

The `SearchAlgorithms.py` module provides implementations of several search algorithms:

- **Breadth-First Search (BFS):** Explores the state space level by level.
- **Depth-First Search (DFS):** Explores the state space depth-first.
- **Depth-Limited Search (DLS):** DFS with a depth limit.
- **Iterative Deepening Search (IDS):** Repeatedly applies DLS with increasing depth limits.
- **Uniform Cost Search (UCS):** Explores paths with the lowest cumulative cost.
- **A* Search:** Uses a combination of actual cost and heuristic estimate to guide the search.

## State Classes

This repository includes various state classes that define problem domains and states:

- `VacuumState`: Represents the state of a vacuum cleaner moving between two rooms.
- `RomaniaState`: Represents states and actions in a navigation problem between cities in Romania.
- `MarsState`: Represents states and actions for navigation on the surface of Mars.
- `HopperState`: Represents states and actions for a hopping creature moving between different heights.

Each state class inherits from the `State` class and provides methods for defining actions, successors, and heuristics.

### `VacuumState`:

Represents the state of a vacuum cleaner moving between two rooms. The class includes methods for actions, successors, and heuristics specific to this problem domain.

### `RomaniaState`:

Represents states and actions in a navigation problem between cities in Romania. Provides methods for defining actions and successors, as well as heuristic functions for A* search.

### `MarsState`:

Represents states and actions for navigation on the surface of Mars. Provides methods for reading graph data and defining actions and successors.

### `HopperState`:

Represents states and actions for a hopping creature moving between different heights. Includes methods for defining actions, successors, and heuristics.

## Heuristic Functions

The `SearchAlgorithms.py` module also includes heuristic functions used in the A* search algorithm:

- `SLD`: Straight Line Distance heuristic for navigation problems.
- `RomaniaSLD`: Heuristic specific to the Romania navigation problem.

These heuristics estimate the cost from a given state to the goal state, guiding the search towards efficient solutions.

## Test Cases

The repository includes test cases to ensure the correctness of the implemented algorithms and state representations. The `TestSearchAlgorithms.py` and `TestHopperState.py` modules contain unit tests for search algorithms and the `HopperState` class, respectively.

## What I Learned

Search Algorithms: I deepened my understanding of various search algorithms commonly used in artificial intelligence and problem-solving. Implementing algorithms like Breadth-First Search, Depth-First Search, A* Search, and others allowed me to grasp their underlying principles and explore their strengths and weaknesses in different scenarios.

State Representation: I learned how to create effective state representations for various problem domains. Designing classes like VacuumState, RomaniaState, MarsState, and HopperState helped me translate real-world scenarios into actionable code. This experience improved my ability to model complex systems and interactions.

Heuristic Functions: Developing heuristic functions such as the Straight Line Distance (SLD) heuristic deepened my understanding of how to guide search algorithms efficiently. These heuristics provided insight into how algorithms can leverage domain-specific knowledge to prioritize promising paths and improve search efficiency.

Unit Testing: Writing comprehensive unit tests for the implemented classes and algorithms enhanced my skills in ensuring code correctness. It taught me to anticipate edge cases, identify bugs, and maintain code quality throughout iterations.

Code Organization: Structuring the project and modularizing code into separate classes and functions improved code readability and maintainability. I learned how to create clean and organized codebases that are easy to understand and extend.

## Usage

To use the provided code, follow these steps:

1. Clone or download this repository to your local machine.
2. Import the necessary classes and functions into your project.
3. Create instances of the state classes and apply the desired search algorithms to solve specific problems.

Example usage can be found in the code comments and the provided sample script.
