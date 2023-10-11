import sys

try:
    if len(sys.argv) == 1:
        exit()
    assert len(sys.argv) == 2, "AssertionError: more than one argument is provided"
    arg = sys.argv[1]
    if arg[0] == '-' and arg[1:].isdigit() or arg.isdigit():
        if int(arg) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else:
        assert False, "AssertionError: argument is not an integer"
except AssertionError as error:
    print(error)