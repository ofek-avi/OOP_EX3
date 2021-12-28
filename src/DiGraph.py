from pip._internal.cli.cmdoptions import src

from src.GraphInterface import GraphInterface
from src.Node_data import node_data


class DiGraph(GraphInterface):
    """

    This class implements GraphInterface interface represents a directional weighted graph.
    can support a large number of nodes (over 100,000).
    The implementation using a dict.
    """

    def __init__(self) -> None:
        """

        :rtype: object
        """
        self.edgesize = 0
        self.MC = 0
        self.Nodes = {}
        self.Edges = {}

    def __eq__(self, o: object) -> bool:
        """
                   Comparison function.
                   """
        if not (isinstance(o, DiGraph)):
            return False
        if not (o.Edges.__eq__(self.Edges)):
            return False
        if not (o.Nodes.__eq__(self.Nodes)):
            return False
        return True

    def v_size(self) -> int:
        """
               Returns the number of vertices in this graph
               @return: The number of vertices in this graph
               """
        return len(self.Nodes)

    def e_size(self) -> int:
        """
               Returns the number of edges in this graph
               @return: The number of edges in this graph
               """

        return self.edgesize

    def __str__(self) -> str:
        """
        This method returns the string representation of the object.
        """

        return f"Graph: | V |= {self.v_size()}, | E |= {self.e_size()}"

    def __repr__(self) -> str:
        """
         returns the object representation in string format.
        """
        return f"Graph: |V|= {self.v_size()}, |E|= {self.e_size()}"

    def get_all_v(self) -> dict:
        """ return a dictionary of all the nodes in the Graph, each node is represented using a pair
                (node_id, node_data)
            """
        return self.Nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
            return a dictionary of all the nodes connected to (into) node_id ,
            each node is represented using a pair (other_node_id, weight)
            """

        if id1 in self.Nodes:
            ans = {}
            for i, j in self.Edges.items():
                if id1 in j:
                    ans[i] = j[id1]
            return ans
        return {}

    def getnode(self, id: int) -> node_data:
        """
                returns the node by the node ID.
        """
        return self.Nodes[id]

    def getEdges(self, src: int, dest: int) -> node_data:
        """
                returns the node by the Edges src and dest.
        """
        return self.Edges[src] + "," + self.Edges[dest]

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
              (other_node_id, weight)
        """
        if id1 in self.Nodes:
            return self.Edges[id1]
        return {}

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """

        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
           Adds an edge to the graph.
           @param id1: The start node of the edge
           @param id2: The end node of the edge
           @param weight: The weight of the edge
           @return: True if the edge was added successfully, False o.w.
           Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """

        if id1 in self.Nodes and id2 in self.Nodes and id2 not in self.Edges[id1]:
            if self.Edges[id1] is None:
                self.Edges[id1] = {}
                self.Edges[id1][id2] = weight
                self.edgesize += 1
                self.MC += 1

            else:
                self.Edges[id1][id2] = weight
                self.edgesize += 1
                self.MC += 1
            return True

        else:
            return False

    def add_node(self, node_id: int , pos: tuple = None,) -> bool:
        """"
          Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """

        n = node_data(id=node_id, p=pos)

        self.Nodes[node_id] = n
        self.Edges[node_id] = {}
        self.MC += 1

    def remove_node(self, node_id: int) -> bool:
        """
                Removes a node from the graph.
                Note: if the node id does not exists the function will do nothing
         """
        if node_id in self.Nodes:
            out = self.all_out_edges_of_node(node_id)
            to = self.all_in_edges_of_node(node_id)
            self.MC += len(self.Edges[node_id])
            self.edgesize -= len(self.Edges[node_id])
            del (self.Edges[node_id])

            for k in to.keys():
                self.remove_edge(k, node_id)
            # self.Edges.pop(node_id)
            self.Nodes.pop(node_id)
            self.MC += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
             Removes an edge from the graph.
             @param node_id1: The start node of the edge
             @param node_id2: The end node of the edge
             @return: True if the edge was removed successfully, False o.w.
             Note: If such an edge does not exists the function will do nothing
        """
        if node_id1 in self.Nodes and node_id2 in self.Nodes and node_id2 in self.Edges[node_id1]:
            self.Edges[node_id1].pop(node_id2)
            self.edgesize -= 1
            self.MC += 1
            return True
        else:
            return False
