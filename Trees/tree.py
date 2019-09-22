
class Tree:
    """Abstract Base Class representing tree structure"""
    class Position:
        """Abstraction representing location of a single element"""

        def element(self):
            """Returns elements stored in this position"""
            raise NotImplemented("must be implemented by subclass")

        def __eq__(self, other):
            """returns True if other position represents same location"""
            raise NotImplemented("must be implemented by subclass")

        def __ne__(self, other):
            """returns Trueif other does not represent the same location"""
            return not (self == other)

    # abstract methods that concrete subclass must support--------------------
    def root(self):
        """return position representing tree's root or None if empty"""
        raise NotImplemented("must be implemented by subclass")

    def parent(self, p):
        """return position representing p's parent (or None if p is root)"""
        raise NotImplemented("must be implemented by subclass")

    def num_children(self, p):
        """return # of children that position p has"""
        raise NotImplemented("must be implemented by subclass")

    def children(self, p):
        """generate iteration of p's children"""
        raise NotImplemented("must be implemented by subclass")

    def __len__(self):
        """return total number of elements in a tree"""
        raise NotImplemented("must be implemented by subclass")

    def is_root(self, p):
        """return true if position p represents root of tree"""
        raise NotImplemented("must be implemented by subclass")

    def is_leaf(self, p):
        """return true if position p does not have any children"""
        raise NotImplemented("must be implemented by subclass")

    def positions(self):
        """generates iterations of tree's positions"""
        raise NotImplemented("must be implemented by subclass")

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        """returns # of levels seperating position p from root
            takes O(n) worse time
        """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self, p):
        """ returns height of subtree rooted at position p
            height of non empty tree T is is max of depth
            of its leaf positions
            Takes O(n^2) worse time
        """
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """returns height of subtre rooted at position p
            takes O(n) time
        """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """returns height of subtree rooted at position p
            params: p (position p, default = None for entire tree height)
        """
        if p is None:
            p = self.root()
        return self._height2(p)


class _BinaryTreeBase(Tree):
    """Abstract class representing binary tree methods"""

    def left(self, p):
        """return position representing p's left child
            return None if p does not have left child
        """
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """return position representing p's right child
            return None if p does not have right child"""

        raise NotImplemented("must be implemented by subclass")

    def sibling(self, p):
        """return position representing p's sibling (None if no siblings)"""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            return self.left(parent)

    def children(self, p):
        """generates an iteration of p's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class BinaryTree(_BinaryTreeBase):
    """Class representing binary tree structure using linked representation
    
    Attributes:
    root:  (Node)       represents root of the binary tree
                        default set to None since its empty at time of creation
    size:   (int)       length of the tree
                        default to 0 since its empty at time of creation
    """

    class _Node:

        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(_BinaryTreeBase.Position):
        """Abstraction representing location of single element"""

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """return element stored at position """
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node


    def _validate(self, p):
        """return position's node or raise appropriate error if invalid"""
        if not isinstance(p, self.Position): raise("p must be proper Position type")
        if p._container is not self: raise ValueError("p does not belong to this container")
        if p._node._parent is p._node: raise ValueError("p is no longer valid")  # convention for deprecated nodes
        return p._node

    def _make_position(self, node):
        """Return Position's instance for a given node"""
        return self.Position(self, node) if node is not None else None

    # binary tree constructor
    def __init__(self):
        """Creates a initially empty binary tree
            takes O(1) time
        """
        self._root = None
        self._size = 0

    def __len__(self):
        """returns total number of nodes in a tree"""
        return self._size 

    def root(self):
        """return root position of tree, return None if tree is empty"""
        return self._make_position(self._root)

    def parent(self, p):
        """return position representing p's parent (or None if p is root)"""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """return position representing p's left child
            return None if p does not have left child
        """
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """return position representing p's right child
            return None if p does not have right child"""

        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """return # of children that position p has"""
        node = self._validate(p)
        count  0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count 

    



