# just a useful function
def are_epsilon_close(a, b, eps=1e-8):
    return abs(a-b) <= eps


def diff(f, x0, h=1e-8):
    return (f(x0+h) - f(x0)) / h  # straight forward but..

    '''
    Approximates the derivative of f at value x0 with some
  (presumabely) small value of h.

  (We can't really take a limit here, but for small enough h
  we should get a good approximation.)
    '''


# x_0: the point where we want to find the slope

def quadratic_func(x):
    return x**2

def test_diff_on_squre_at_1():
    d = diff(quadratic_func, 1, 1e-8)
    assert are_epsilon_close(2, d, eps=1e-5)

# assert > checking if the calculated derivative d is whithin 10^-5 of the expected value, which is 2.
