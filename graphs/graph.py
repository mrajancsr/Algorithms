"""Implementation of Graphs using adjacency list, edge list, adjacency map and adjacency matrix
Author: Raj Subramanian
Date: July 20, 2020
"""
from base import GraphBase

class GraphEdgeList(GraphBase):
    """implementation of Graph via EdgeList
    Args: 
    None

    Returns: 
    Graph in a list format
    """
    class _Vertex(GraphBase.VertexBase): 
        def __init__(self, x, pos=None):
            self._value = x 
            self._pos = pos 
    
    class _Edge(GraphBase.EdgeBase): 
        def __init__(self, u, v, x=None, pos=None):
            self._start = u 
            self._end = v 
            self._value = x 
            self._pos = pos 
    # - nested Vertex Class
    def __init__(self):
        self._V = PositionalList()
        self._E = PositionalList()
    
    def add_vertex(self, x):
        u = self.Vertex(x)
        p = self._V.add_first(u)
        u._pos = p 
        return u
    
    def add_edge(self, u, v, x):
        e = self.Edge(u, v, x)
        p = self._E.add_first(e)
        e._pos = p
        return e
    
class GraphAdMap:
    """implementation of a graph using adjacency map
    For a pair of vertices (u,v), (u,z) that has an edges E, F
    is represented by {u: {v: E, z: F}}"""

    """nested Vertex and Edge classes"""
    class _Vertex: 
        """vertex structure for graph"""
        __slots__ = '_value'

        def __init__(self, val):
            self._value = val
        
        def get_value(self):
            """return value associated with this vertex"""
            return self._value 
        
        def __hash__(self):
            """allows vertex to be a key in a dictionary"""
            return hash(id(self))
        
        def __repr__(self):
            return """Vertex({!r})""".format(self._value)
    
    # --  nested edge class
    class _Edge:
        """Implements the edge structure that returns edge associated
            with vertex (u,v)
        """
        # light weight edge structure
        __slots__ = '_start', '_end', '_value'

        def __init__(self, u, v, val):
            self._start = u 
            self._end = v 
            self._value = val 
        
        def __repr__(self):
            insert = (self._start, self._end, self._value)
            return """Edge(({!r}, {!r}): {:.2f}""".format(*insert)
        
        def endpoint(self):
            """return (u,v) as a tuple for vertices u and v"""
            return (self._start, self._end)
        
        def opposite(self, u):
            """return vertex opposite of u on this edge"""
            return self._end if u is self._start else self._start
        
        def get_value(self):
            """return value associated with this edge"""
            return self._value 
        
        def get_items(self):
            """returns edge attributes as a tuple
            Helpful for visualizing nodes and their edge weights"""
            return (self._start._value, self._end._value, self._value)
        
        def __hash__(self):
            return hash((self._start, self._end))
    
    # -- beginning of graph definition
    def __init__(self, directed=False):
        """create an empty graph undirected by default
        Graph is directed if parameter is set to True
        """
        self._out = {}
        self._in = {} if directed else self._out
    
    def is_directed(self):
        """return True if graph is directed, False otherwise"""
        return self._in is not self._out
    
    def count_vertices(self):
        """returns the count of total vertices in a graph"""
        return len(self._out)
    
    def get_vertices(self):
        """returns iteration of vertices keys"""
        return self._out.keys()
    
    def count_edges(self):
        """return count of total edges in a graph"""
        total_edges = sum(len(self._out[v]) for v in self.get_vertices())
        return total_edges if self.is_directed() else total_edges // 2
    
    def get_edge(self, u, v):
        """returns the edge between u and v, None if its non existent"""
        return self._out[u].get(v)
    
    def get_edges(self):
        """returns iteration of all unique edges in a graph"""
        seen = set()
        for inner_map in self._out.values():
            seen.update(inner_map.values())
        return seen 
    
    def degree(self, u, outgoing=True):
        """return total outgoing edges incident to vertex u in the graph
        for directed graph, optional parameter counts incoming edges
        """
        temp = self._out if outgoing else self._in 
        return len(temp[u])
    
    def incident_edges(self, u, outgoing=True):
        """returns iteration of all outgoing edges incident to vertex u in this graph
        for directed graph, optional paramter will receive incoming edges
        """
        temp = self._out if outgoing else self._in 
        for edge in temp[u].values():
            yield edge 
    
    def insert_vertex(self, val=None):
        """insert and return a new vertex with value val"""
        u = self._Vertex(val)
        self._out[u] = {}
        if self.is_directed():
            self._in[u] = {}
        return u 
    
    def insert_edge(self, u, v, val=None):
        """insert and return a new edge from u to v with  value val (identifies the edge)"""
        edge = self._Edge(u,v,val)
        self._out[u][v] = edge 
        self._in[v][u] = edge
    
         
    
        
