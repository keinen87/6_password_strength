import string
import sys


def get_password_strength(password):
    score = 0
    content = [bool([symbol for symbol in password if symbol in string.ascii_lowercase]) \
    for symbols_kit in [string.ascii_lowercase,string.ascii_uppercase,string.digits,string.punctuation]]
    score = 2.5 * len(content)
    return score


if __name__ == '__main__':
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print('Password strength: {0}'.format(str(get_password_strength(password))))
    else:
        print('Error! Enter password!')
