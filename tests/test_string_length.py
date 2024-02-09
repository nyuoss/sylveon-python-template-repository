# Some basic test for string length

from sylveon.string_length.find_length import find_length

def test_string_length_succeed(capsys):
    find_length("Hello World!")
    captured = capsys.readouterr()

    assert captured.out == "Length of string Hello World! is 12\n"
