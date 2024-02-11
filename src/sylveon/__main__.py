# Example showing how to import different components of the package and use them in the main function

from sylveon._hello._greeting import hello_world
from sylveon.string_length.find_length import find_length


def main():
    greeting = hello_world()
    print(greeting)
    length_str = find_length(greeting)
    print(f"Length of string {greeting} is {length_str}")


if __name__ == "__main__":
    main()