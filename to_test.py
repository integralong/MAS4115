
# function to test
def double(x):
    '''
    returns twice the argument x; x is unchanged
    '''
    return x*2

# function to test
def test_double_on_zero():
    assert double(0) == 0
def test_double_on_integer():
    assert double(2) == 3
def test_double_on_string():
    assert double("a") == "aa"
def test_double_on_empty_string():
    assert double("") == ""    
