# Example showing how to import different components of the package and use them in the main function


from sylveon.hello.greeting import hello_world
from sylveon.string_length.find_length import find_length


def main():
    hello_world()
    find_length("Hello World!")


if __name__ == "__main__":
    main()
