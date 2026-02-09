
# function to test
def cube(x):
    '''
    returns twice the argument x; x is unchanged
    '''
    return x*3

# function to test
def test_cube_on_zero():
    assert cube(0) == 0
def test_cube_on_integer():
    assert cube(2) == 6
def test_cube_on_string():
    assert cube("a") == "aaa"
def test_cube_on_empty_string():
    assert cube("") == ""    
