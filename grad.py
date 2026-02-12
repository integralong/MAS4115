def are_epsilon_close(a, b, eps=1e-8):
    return abs(a - b) <= eps

def grad(f, x0, y0, h=1e-8):
    dfdx = (f(x0 + h, y0) - f(x0, y0)) / h
    dfdy = (f(x0, y0 + h) - f(x0, y0)) / h
    return (dfdx, dfdy)

def circle(x, y):
    return x**2 + y**2

def test_grad_circle():
    g = grad(circle, 1, 2, h=1e-6)
    assert are_epsilon_close(g[0], 2, eps=1e-5)
    assert are_epsilon_close(g[1], 4, eps=1e-5)
