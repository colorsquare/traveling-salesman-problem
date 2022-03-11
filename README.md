# Traveling Salesman Problem

Traveling salesman problem, also known as TSP, approached with genetic algorithms in CS454, KAIST, 2019 Fall.

## About the course and the problem

Please refer to the [course homepage](https://coinse.kaist.ac.kr/teaching/2019/cs454/).
More information about traveling salesman problem can be found [here](https://en.wikipedia.org/wiki/Travelling_salesman_problem).

## About the code

Classical optimization algorithms such as greedy search are not effective due to high computation cost in large problem instances. There's currently no known single best algorithm for traveling salesman problem, and various stochastic optimizations are proposed. These solutions does not aim for the 'answer', but shows sufficient optimization with great efficiency.

The classic, and meta-heuristic approaches are as follows:

[greedy search](https://en.wikipedia.org/wiki/Greedy_algorithm), [2-opt](https://en.wikipedia.org/wiki/2-opt), [genetic algorithms](https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3), [ant-colony optimization (ACO)](http://www.scholarpedia.org/article/Ant_colony_optimization), [particle swarm optimization (PSO)](https://en.wikipedia.org/wiki/Particle_swarm_optimization), and more: [lin-kernigan heuristic](http://www.akira.ruc.dk/~keld/research/LKH/), [concorde](http://www.math.uwaterloo.ca/tsp/concorde/gui/gui.htm)

## Getting started

Before starting, refer to the section [Preparing for pickle data](#preparing-for-pickle-data) to generate .pickle files.

### main
```sh
$ python3 main.py                   # default: genetic-algorithm with rl11849
$ python3 main.py 2opt a280         # receives two positional arguments of method and data
```

### method modules
```sh
$ python3 example_module.py         # default data: a280
$ python3 example_module.py a280    # receives one positional argument data
```

## Folder structure
```sh
traveling-salesman-problem
├── README.md
├── .gitignore
├── tsp.py                          # class TSP
├── data/
│   ├── tsp_to_pickle.py            # transforms mp-testdata to .pickle
│   ├── mp-testdata/
│   │   ├── a280.tsp
│   │   ├── rl11849.tsp
│   │   └── ...
│   ├── a280_coordinates.pickle     # generate with tsp_to_pickle.py
│   ├── a280_distances.pickle       # generate with tsp_to_pickle.py
│   └── ...
├── heuristics/
│   ├── greedy_search.py
│   ├── two_opt.py
│   └── genetic_programming.py
└── main.py                         # choose a data file, and execute with desired method
```

## Data and testings

### Raw datasets

The basic dataset used for testings in this problem is [MP-TESTDATA](http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/index.html). The numbers in file name denotes the number of cities.

### Preparing for .pickle data

For detailed operations, refer to [tsp_to_pickle.py](data/tsp_to_pickle.py)

```sh
$ cd data                           # switch directory for proper execution of tsp_to_pickle.py
$ python3 tsp_to_pickle.py a280     # receives one positional argument data
$ cd ../..                          # return to main
```


<!-- ## Interesting TSP approaches -->

<!--
[https://www.researchgate.net/post/What_is_the_best_soft-computing_algorithm_used_to_solve_TSP_Problem_the_travelling_salesman_problem2](https://www.researchgate.net/post/What_is_the_best_soft-computing_algorithm_used_to_solve_TSP_Problem_the_travelling_salesman_problem2)
-->
