import nnvm.symbol as sym

def test_fullc():
    x = sym.Variable('x')
    x1 = sym.dense(x, units=3, name="dense")
    x2 = sym.flatten(x1)
    x3 = sym.softmax(x2)
    assert x2.list_input_names() == ['x', 'dense_weight', 'dense_bias']

def test_concatenate():
    x = sym.Variable('x')
    y = sym.Variable('y')
    y = sym.concatenate(x, y)
    assert y.list_input_names() == ['x', 'y']

def test_unary():
    x = sym.Variable('x')
    x = sym.exp(x)
    x = sym.log(x)
    x = sym.sigmoid(x)
    x = sym.tanh(x)
    assert x.list_input_names() == ['x']

def test_batchnorm():
    x = sym.Variable('x')
    x = sym.batch_norm(x, name="bn")
    assert x.list_input_names() == [
        "x", "bn_gamma", "bn_beta", "bn_moving_mean", "bn_moving_var"]


if __name__ == "__main__":
    test_concatenate()
    test_fullc()
    test_unary()
    test_batchnorm()
