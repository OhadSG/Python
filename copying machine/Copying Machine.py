READ_FROM = r"C:\Users\User\Desktop\python cyber\copying machine\f.txt"
WRITE_TO = r"C:\Users\User\Desktop\python cyber\copying machine\e.txt"


def main():
    copy_file_to(READ_FROM, WRITE_TO)
    print_file(WRITE_TO)


def copy_file_to(copy_from, copy_to):
    with open(copy_from, "r") as read_from:
        with open(copy_to, "w") as write_to:
            for line in read_from:
                write_to.write(line, )


def print_file(file):
    with open(file, "r") as file:
        for line in file:
            print(line, )


if __name__ == '__main__':
    main()
