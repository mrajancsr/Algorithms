import pytest 

def capitalize_case(x):
    if not isinstance(x, str): raise TypeError("Please provide a string argument")
    return x.capitalize()

def test_capital_case():
    assert capitalize_case("semaphore") == "Semaphore"

def test_raises_exception_on_non_string_arguments():
    """checks for any non string arguments"""
    with pytest.raises(TypeError):
        capitalize_case(9)
