# *****************************************************
# Lazy Student.py
# Ohad Solomon Gleicher
# 26.10.2020
#
# Summary:
#   Gets a txt file with mathematical exercises in it and writes the answers to another txt file
#   Both files are received as parameters
# *****************************************************

import sys
import os

QUESTIONS = 1
ANSWERS = 2

NUM1 = 0
OPERATOR = 1
NUM2 = 2

OPERATORS = ['+', '-', '/', '*']


def main():
    if check_params(QUESTIONS, ANSWERS):
        q = os.path.abspath(sys.argv[QUESTIONS])
        a = os.path.abspath(sys.argv[ANSWERS])
        with open(q, "r") as questions, open(a, "w") as answers:
            for question in questions:
                question = question.rstrip()
                if check_question(question):
                    answers.write('{} = {}\n'.format(question, solve_question(question)))
                else:
                    answers.write("Question ({}) is not in the correct format\n".format(question))
    else:
        print("Invalid parameters")

    assert check_params(1, 2) is True
    assert check_params(0, 2) is True
    assert check_params(1, 3) is False

    assert check_question("1 + 1") is True
    assert check_question("1 - 1") is True
    assert check_question("1 * 1") is True
    assert check_question("1 / 1") is True
    assert check_question("1+ 1") is False
    assert check_question("1+1") is False
    assert check_question("1 +1") is False
    assert check_question("asdf") is False  # ASDF MOVIE - GO WATCH!!

    assert solve_question("1 + 1") == 2
    assert solve_question("1 - 1") == 0
    assert solve_question("1 * 1") == 1
    assert solve_question("1 / 1") == 1
    assert solve_question("3 / 2") == 1.5
    assert solve_question("1 / 0") == "ERROR: division by 0"


def check_params(arg1, arg2):
    """ Checks if the two files exist

    Return:
        True if the 2 files exist
        False if not

    """
    if len(sys.argv) >= (arg2 + 1):
        questions_exist = os.path.exists(os.path.abspath(sys.argv[arg1]))
        answers_exist = os.path.exists(os.path.abspath(sys.argv[arg2]))
        if not questions_exist or not answers_exist:
            return False
        else:
            return True
    else:
        return False


def check_question(question):
    """ Checks if the question in in the correct format

    Format: "[Number] [Operator] [Number]"
    #Operator must be in ['+', '-', '/', '*']

    Parameters:
        question: a string containing the question

    Returns:
        True if the question is of the correct format
        False if not
    """
    parts = question.split()
    if len(parts) == 3:
        if parts[NUM1].isdigit() and parts[OPERATOR] in OPERATORS and parts[NUM2].isdigit():
            return True
    return False


def solve_question(question):
    """ Solves a mathematical expression of the format [Number] [Operator] [Number] and returns the result

    Parameters:
        question: a string containing a mathematical expressing of the mentioned format

    Returns:
        The result of the expression (Number)

    """
    parts = question.split()
    num1 = parts[NUM1]
    num2 = parts[NUM2]

    if parts[OPERATOR] == '+':
        return num1 + num2
    elif parts[OPERATOR] == '-':
        return num1 - num2
    elif parts[OPERATOR] == '*':
        return num1 * num2
    else:
        if num2 != 0:
            return num1 / num2
        else:
            return "ERROR: division by 0"


if __name__ == '__main__':
    main()
