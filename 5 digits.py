def main():
    x = input("Please enter a 5 digit number\n")
    print('you entered the number: {}'.format(x))
    print('The digits of this number are: {}'.format(','.join([i for i in x])))
    print('The sum of the digits is: {}'.format(str(sum([int(i) for i in x]))))


if __name__ == '__main__':
    main()
