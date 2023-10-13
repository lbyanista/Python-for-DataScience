import sys

def main():
    """program calcul the total character and the number of capital letters and lower letters and also the punctutaion marks and how many spaces and how many digits in a string"""

    if len(sys.argv) == 2:
        if sys.argv[1] == "--help":
            print("Usage: python3 building.py <a string>")
            return
        else:
            string = sys.argv[1]
    elif len(sys.argv) == 1:
        string = input("What is the text to count?\n")
    else:
        try:
            assert False, "AssertionError: too many arguments"
        except AssertionError as error:
            print(error)
            return

    total = 0
    upper = 0
    lower = 0
    punct = 0
    space = 0
    digit = 0

    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isspace():
            space += 1
        elif char.isdigit():
            digit += 1
        elif char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            punct += 1
        total += 1

    print("The text contains", total, "characters:")
    print("-", upper, "upper letters")
    print("-", lower, "lower letters")
    print("-", punct, "punctuation marks")
    print("-", space, "spaces")
    print("-", digit, "digits")

if __name__ == '__main__':
    main()