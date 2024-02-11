# Some basic test for string length

from sylveon.string_length.find_length import find_length

def test_string_length_succeed():
    string = "Hello World!"
    l = find_length(string)

    assert l == len(string)
