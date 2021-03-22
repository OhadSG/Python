STRING_LEN = 5


def check_input(x):
    """ Checks if the input x is a 5 digit number and returns the result
    Parameters:
        x - a string
    Return:
        The outcome of the boolean statement (T/F)
    """

    if x.isdigit() and len(x) == STRING_LEN:
        return True
    return False


def de_javu(x):
    """ The function gets string and checks if it's a 5 digit number.
    if yes it returns a tuple with the number itself, the digits of the
    number separated by a ',' and the sum of the digits of the number.

    Parameters:
        x - string

    Return:
        x (The parameter)
        THE_DIGITS - The digits of x separated by ',' (string)
        THE_SUM - The sum of the digits of the parameter x (string)
    """
    if not check_input(x):
        return None

    THE_DIGITS = ','.join([i for i in x])
    THE_SUM = str(sum([int(i) for i in x]))
    return x, THE_DIGITS, THE_SUM


def main():
    while (result := de_javu(input("Enter a 5 digit number: "))) is None:
        continue
    THE_NUMBER, THE_DIGITS, THE_SUM = result
    print('you entered the number: {}'.format(THE_NUMBER))
    print('The digits of this number are: {}'.format(THE_DIGITS))
    print('The sum of the digits is: {}'.format(THE_SUM))

    assert de_javu("ABCDE") is None
    assert de_javu("ABCD") is None
    assert de_javu("1234") is None
    assert de_javu("12345") == ("12345", "1,2,3,4,5", "15")
    assert de_javu("11111") == ("11111", "1,1,1,1,1", "5")


if __name__ == "__main__":
    main()
