# Exercises 3

In this exrcises we implemented uninformed search algorithms BFS, DFS, UCS in order to solve the problem of Romanian cities.

## Files

- `exercises3.pdf` - contains the text of the problem for this week's exercises
- `RomanianMap/template/` - this directory contains templates for the search algorithms that we will be using in this exercises as the starting point for our implementation

- `RomanianMap/implementation/` - this directory contains the solution if this exercises
    - `search_algorithms/` - this directory contains the implementation of the search algorithms engine that we implemented in this exercises
        - `interfaces.py` - this file contains the interfaces need for problem formulation (implemented on last exercises) 
        - `problem.py` - this file contains the class that encapsulates the problem definition (implemented on last exercises)
        - `node.py` - this file contains the implementation of the nodes that we use in search algorithms
        - `search.py` - this file contains the abstract class defining the template for all search algorithms
        - `bfs.py` - this file contains the implementation of the BFS algorithm
        - `dfs.py` - this file contains the implementation of the DFS algorithm
        - `ucs.py` - this file contains the implementation of the UCS algorithm
    - `city_connections.txt` - file containing the connections between cities
    - `straight_line_distances.txt` - file containing the straight line distances between cities
    - `romanian_map.py` - this script defines the class which loads city data from the given files above
    - `problem_definition.py` - this file contains the implementation of the problem definition for the Romanian cities problem
    - `main.py` - this file contains the main function that runs the search algorithms on the problem
