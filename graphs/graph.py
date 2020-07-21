"""Implementation of Graphs using adjacency list, edge list, adjacency map and adjacency matrix
Author: Raj Subramanian
Date: July 20, 2020
"""
from linked_lists.linked_collections import PositionalList
class GraphEdgeList:
    """implementation of Graph via EdgeList
    Args: 
    V: a collection of vertices 
    E: collection of edges stored in (u,v) pairs

    Returns: 
    Graph in a list format
    """
    class Vertex: 
        def __init__(self, x, pos=None):
            self._element = x 
            self._pos = pos 
    
    class Edge: 
        def __init__(self, u, v, x=None, pos=None):
            self._start = u 
            self._end = v 
            self._element = x 
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
    
         
    
        
