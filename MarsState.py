from Graph import Graph, Edge, Node
from State import State


class MarsState(State) :
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, cost=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.cost = cost

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.cost < other.cost

    def __le__(self, other):
        return self.cost <= other.cost

    def is_goal(self):
        return self.location == '1,1'

    ## print in reverse
    def print_solution(self):
        ptr = self
        print(ptr)
        while ptr:
            print(ptr.prev_state)
            ptr = ptr.prev_state

    def successors(self):
        edges = self.mars_graph.get_edges(self.location)
        return [MarsState(edge.dest, self.mars_graph, self,
                                     self.cost + edge.val)
                        for edge in edges]


    ## you implement this. Open the file filename, read in each line,
    ## construct a Graph object and assign it to self.mars_graph().
    def read_mars_graph(self, filename):
        graph = Graph()
        nodes = []
        edges = []
        with open(filename, "r") as file:
            for line in file:
                node, adjacents = line.strip().split(":")
                print("Node: " + node + " Connections: " + adjacents)
                n = Node(node)
                graph.add_node(n)
                connections = adjacents.split(" ")
                for connection in connections:
                    edge = Edge(node, connection)
                    edges.append(edge)
        # print(nodes)
        # print(edges)
        # for n in nodes:
        #     graph.add_node(n)
        # for edge in edges:
        #     graph.add_edge(edge)
        self.mars_graph = graph

if __name__=="__main__" :
    s = MarsState()
    s.read_mars_graph("MarsMap")
    print(s.mars_graph.g)