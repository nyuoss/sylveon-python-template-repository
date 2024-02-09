# Test package and make sure it prints "Hello World"


def test_hello_world(capsys):
    from sylveon.hello.greeting import hello_world

    # call the function
    hello_world()
    captured = capsys.readouterr()

    # compare stdout with expected output
    assert captured.out == "Hello World!\n"
