
# function to test
def triple(x):
    '''
    returns twice the argument x; x is unchanged
    '''
    return x*3

# function to test
def test_cube_on_zero():
    assert triple(0) == 0
def test_cube_on_integer():
    assert triple(2) == 6
def test_cube_on_string():
    assert triple("a") == "aaa"
def test_cube_on_empty_string():
    assert triple("") == ""    
