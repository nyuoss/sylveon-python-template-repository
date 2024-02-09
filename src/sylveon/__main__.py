# this file will change our package into a runnable module
# recommended not to use "if __name__ == __main__" pattern
# when importing from package.__main__, __name__ will include the package name
# but importing from __main__ has a different meaning


from src.sylveon.hello.greeting import hello_world
from src.sylveon.string_length.find_length import find_length


def main():
    hello_world()
    find_length("Hello World!")


if __name__ == "__main__":
    main()
