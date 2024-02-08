# this file will change our package into a runnable module
# recommended not to use "if __name__ == __main__" pattern
# when importing from package.__main__, __name__ will include the package name
# but importing from __main__ has a different meaning


def hello_world():
    return "Hello World"


if __name__ == "__main__":
    print(hello_world())

# change this to do component stuff
