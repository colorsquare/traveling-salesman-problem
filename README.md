# Traveling Salesman Problem

Traveling salesman problem, also known as TSP, approached with genetic algorithms and others. Based on CS454, KAIST, 2019 Fall.

## About the Course and the Problem

Please refer to the [course homepage](https://coinse.kaist.ac.kr/teaching/2019/cs454/).
More information about traveling salesman problem can be found [here](https://en.wikipedia.org/wiki/Travelling_salesman_problem).

## About the Code

Classical optimization algorithms such as greedy search are not effective due to high computational cost in large problem instances of traveling salesman problem. There's currently no known single best algorithm, and instead, various stochastic optimizations are proposed. These solutions does not aim for the '*answer*', but shows sufficient level of optimization with great efficiency.

The classic and meta-heuristic approaches are as follows:

[Greedy Search](https://en.wikipedia.org/wiki/Greedy_algorithm), [2-Opt](https://en.wikipedia.org/wiki/2-opt), [Genetic Algorithms](https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3), [Ant-Colony Optimization (ACO)](http://www.scholarpedia.org/article/Ant_colony_optimization), [Particle Swarm Optimization (PSO)](https://en.wikipedia.org/wiki/Particle_swarm_optimization)  
And more: [Lin-Kernigan Heuristic](http://www.akira.ruc.dk/~keld/research/LKH/), [Concorde](http://www.math.uwaterloo.ca/tsp/concorde/gui/gui.htm)

## Getting Started

```sh
$ python3 main.py                   # default: genetic-algorithm with rl11849
$ python3 main.py 2opt a280         # receives two positional arguments of method and data
```

