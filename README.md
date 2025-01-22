# Genetic vs swarm algorithm comparison for n-traveling salesman problem 

This project aims to compare results for genetic and swarm algorithm.

## Table of Contents

- [Installation](#installation)
- [Problem](#Problem)
- [Robot](#Robot)
- [Node](#Node)
- [Results](#Results)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AiR-ISZ-Gr1/deep_learning.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
## Problem

The problem is similar to the n-traveling salesman problem with added constraints. Autonomous robots, acting as salesmen, navigate a warehouse graph where distances between shelves are edge weights. Their goal is to collect and deliver specified items to a collection point. Each robot has a capacity and a speed inversely proportional to its load, requiring optimal configurations based on the load.

Robots start from a common point, pick products from designated shelves, and deliver them to the packing area. The order specifies which shelves (vertices) have the needed products and their quantities. Only necessary vertices are considered to reduce complexity.

The solution measures the time from order receipt to completion. To minimize this time, each robot's path is optimized. Robots' capacities introduce a knapsack problem, requiring efficient product distribution to avoid overloading and minimize returns to the collection point. The goal is to minimize order completion time by effectively using all robots.

## Robot
1. id
2. velocity 
3. capacity
4. list of elements to carry

## Node
1. id
2. weight of one element

## Results

### Swarm 1

![image](https://github.com/wasikjakub/genetic-and-swarm-algorithm-comparison/assets/144064944/0267c467-b4c8-4a78-98c6-130d3a15c715)

![image](https://github.com/wasikjakub/genetic-and-swarm-algorithm-comparison/assets/144064944/9d9d40c8-b0ae-4fae-9a94-76d7dc88f0cc)

### Genetic 1

![image](https://github.com/wasikjakub/genetic-and-swarm-algorithm-comparison/assets/144064944/c199f583-f3f0-4fa8-9775-f319b8c6f4a1)

### Swarm 2

![image](https://github.com/wasikjakub/genetic-and-swarm-algorithm-comparison/assets/144064944/3660a583-5c87-4785-95ee-46ccb514c2e2)

![image](https://github.com/wasikjakub/genetic-and-swarm-algorithm-comparison/assets/144064944/25872b2e-1cb7-4008-a79e-8df17574b70f)

### Genetic 2

![image](https://github.com/wasikjakub/genetic-and-swarm-algorithm-comparison/assets/144064944/4f1095be-492e-45c8-b80f-4eec4c0bc64a)

## Additional Authors

Huge thanks for contributions for: 
- @ttarnawski
- @michalsciubisz
- @WojtekTok
- @adam-filapek
- @if-netizen
- @rkeere
- @BartoszBar
