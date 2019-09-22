from math import sqrt
class Vector:
    """Custom vector class"""
    def __init__(self, d):
        """Create a d-dimension vector of zeros"""
        self._coords = [0] * d

    def __len__(self):
        """returns the length of the vector"""
        return len(self._coords)

    def __getitem__(self, j):
        """Returns jth coordinate of vector"""
        return self._coords[j]

    def __setitem__(self, j, val):
        """sets the jth coordinate of vector to given value"""
        self._coords[j] = val
    def __add__(self, vec):
        """return sum of two vectors"""
        return Vector(list(map(lambda x,y: x+y, self._coords,vec._coords)))

    def __repr__(self):
        """returns string representation of the vector"""
        return repr(self._coords)

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other  # rely on existing __eq__ definition

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'
    def __gt__(self, other):
        """checks to see if norm of a vector is greater than the other"""
        val1 = sqrt(sum(x*x for x in self._coords))
        val2 = sqrt(sum(x*x for x in other._coords))
        return val1 > val2