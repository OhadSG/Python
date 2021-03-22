import sys

POSITION = 1


def main():
    with open(sys.argv[POSITION], "r") as read_from:
        print_file(read_from)


def print_file(file):
    for line in file:
        print(line, )


if __name__ == '__main__':
    main()
