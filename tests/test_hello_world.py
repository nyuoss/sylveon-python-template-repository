# Test package and make sure it prints "Hello World"


def test_hello_world():
    from sylveon._hello._greeting import hello_world

    # call the function
    hello = hello_world()

    assert hello == "Hello World"
