def test_sum():
    """tests if sum of numbers 1,2,3 is 6"""
    assert sum([1,2,3]) == 6, "should be 6"

def test_sum_tuple():
    assert sum((1,2,3)) == 6, "should be 6"

#  Notice compared to test_sum_unittest.py which uses 
# the unittest test runner, we convert test sum into 
# classes and test it.  using pytest, we don't need
# to conert it to a seperate testing classes.  

#  nor do we need a command line entry  point
