# Ex3

@authers Ofek Avi Saadon & Yuval Bar-Maoz

### *introduction*

This project is about directed weighted graphs.
Directed weighted graphs are (simple) directed graphs with weights assigned to their edges.
The graph id loaded by json file.
We asked to implement interfaces of directed weighted graphs and of directed weighted graphs algorithms, and to represent the graphs by GUI presentation.


### *Project Materials*

For understanding all the problem space we assisted the videos of William Fiset and wikipedia:

https://www.youtube.com/channel/UCD8yeTczadqdARzQUp29PJw
https://en.wikipedia.org/wiki/Directed_graph
https://en.wikipedia.org/wiki/Graph_center
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

Also, for few of the algorithms implementations we assisted GeeksForGeeks and StackOverFlow forums.
https://www.geeksforgeeks.org/
https://stackoverflow.com/


### *UML of the project*


![image](https://user-images.githubusercontent.com/92522577/147612354-bdbac38c-329c-4b79-9406-e767954072ab.png)

This UML diagram represent the main classes in the project.

Arrow with dashed line between Interface to Class mean that the Class implement the Interface.

Arrow with solid line between two Classes mean that this class depends on the other class.

The green points mean functions from the interface and the black points mean that this is a function that added by us for the project.

### *Explanation on the classes*

#### __main__
The main get json file and create a graph, this graph implements by the algorithms graph, and the function runGui create GUI presentation of this algorithms graph.


#### __DiGraph__

Implement of the Abstract Class GraphInterface and representing a graph with the follows methods:

    v_size -> return int: number of nodes in the graph
    e_size -> return int: number of edges in the graph
    get_all_v -> return dict: dictionary of all the nodes in the graph
    all_in_edges_of_node -> return dict: dictionary of all the edges whom go into specific node
    all_out_edges_of_node -> return dict: dictionary of all the edges whom go out of specific node
    get_mc -> return int: represent the number of changes the graph had
    add_edge -> return bool: add edge to the graph
    add_node -> return bool: add node to the graph
    remove_node -> return bool: remove node from the graph
    remove_edge -> return bool: remove edge from the graph


More functions in Digraph that are not implement of GraphInterface:

    getEdgeBySrc -> return list: Listing all the neighbors of specific node
    getWeightOfEdge -> return float: return the weight of an edge



#### __GraphAlgo__

Implement of the Abstract Class GraphInterface:

    get_graph -> DiGraph: Return the current graph
    load_from_json -> bool: Load graph from json file
    save_to_json -> bool: Save graph to json file
    shortest_path -> (float, list): Return the shortest path from one node to another
    TSP -> (List[int], float): Finds the shortest path that visit all the nodes in the list.
    centerPoint -> (int, float): Finds the node that has the shortest distance to it's farthest node.
    plot_graph -> None: Plot the graph


More functions in GraphAlgo that are not implement of GraphInterface:

    Dijkstra -> 
    find_way -> list: Find the best circle permute for node. (helper functions for TSP)
    relax ->



#### __NodeData__

    getkey -> : Return the id associated with the node
    gettag -> : Return the temporal data in the node
    getweight -> : Returns the weight associated with this node
    getinfo -> : Returns the data within this node
    settag -> : Allows setting the "tag" value for temporal marking a node
    setweight -> : Allows changing the node weight
    setinfo -> : Allows changing the node data
    getlocation -> : Return the location of the node
    setlocation -> :Allows changing the node location


###Compare to Ex2

![image](https://user-images.githubusercontent.com/92522577/147612182-bd621b64-b78f-4c3d-b59c-5f62018d5648.png)

more compare you can see at the [TestGraphAlgo](https://github.com/ofek-avi/OOP_EX3/blob/main/test/TestGraphAlgo.py).

