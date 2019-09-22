
class Progression:
    """Iterator producing generic progression

    Default iterator produces hwole numbers."""

    def __init__(self, start=0):
        """Initialize current to value of progression"""
        self._current = start

    def _advance(self):
        """Update self._current to a new value

        This should be overriden in subclass to customize progression

        By convention, if current is set to None, this designes the
        end of a finite progression
        """
        self._current += 1

    def __iter__(self):
        """By convention, an iterator must return self as a iterator"""
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))


class ArithemeticProgression(Progression):
    """iterator procuding an arithematic progression"""

    def __init__(self, increment=1, start=0):
        """Create arithematic progression

        increment: fixed constant to add to each term (default=1)
        start: the first term of the progression(default 0)
        """
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        """Update current value by adding the fixed increment"""
        self._current += self._increment


class GeometricProgression(Progression):
    """Iterator producing geometric progression"""

    def __init__(self, const=2, start=1):
        """Create a geometric progression

        const:  the fixed constant multiplied to each term (default=2)
        start:  the first term of the progression (default=1)
        """
        super().__init__(start)
        self._constant = const

    def _advance(self):
        """update curent value by multiplying it by const value"""
        self._current *= self._constant


class FibonacciProgression(Progression):
    """Create fibonacci progression"""

    def __init__(self, first=0, second=1):
        """Create a new fibonacci sequence

        first:  the first term of the progression (default=0)
        second: the second term of the progression (default=1)
        """
        super().__init__(first)  # start progression at first
        self._prev = second - first # fictious value before the progression

    def _advance(self):
        """update current value by taking the sum of first two"""
        self._prev, self._current = self._current, self._prev + self._current

#  abstract base class
from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    """my own version of collections.Sequence abstract base class"""

    @abstractmethod
    def __len__(self):
        """return length of the sequence"""

    @abstractmethod
    def __getitem__(self,j):
        """Return the element at index j of the sequence"""

    def __contains__(self,val):
        """return true if val found in the sequence; false otherwise"""
        for j in range(len(self)):
            if self[j] == val:
                return True 
        return False 

    def index(self, val):
        """return index of where val is found"""
        for i,j in enumerate(self):
            if j == val:
                return i 
        raise ValueError("value not in sequence")

    def count(self, val):
        """return number of elements equal to a given value"""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k 
    
