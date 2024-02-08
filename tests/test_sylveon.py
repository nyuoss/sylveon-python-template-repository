# Test package and make sure it prints "Hello World"


def test_hello_world():
    from sylveon import __main__

    assert __main__.hello_world() == "Hello World"
