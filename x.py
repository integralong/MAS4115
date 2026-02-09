
def sub(a,b):
    '''
    Remember that both a and b are vectors, represented as tuples (a-b)
    '''
    return (b[0] - a[0], b[1] - a[1])


def test_sub_zero():
    zero_vector = (0,0)
    assert sub(zero_vector, zero_vector) == zero_vector

def test_sub_positive():
    a = (4, 2)
    b = (6, 4)
    assert sub(a,b) == (2,2)

def test_sub_negative():
    a = (-1, 1)
    b = (-2, 3)
    assert sub(a,b) == (-1,2)


