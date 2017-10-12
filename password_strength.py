import getpass
import string
import os


def load_blacklist(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as textfile:
        blacklist = [line.strip() for line in textfile]
        return blacklist


def get_password_strength(password, blacklist):
    score = 0
    min_length_bound = 5
    max_lenght_bound = 8
    if password in blacklist or len(password) < min_length_bound:
        return score
    has_lowercase_symbols = any(symbol in string.ascii_lowercase
                                for symbol in password)
    has_uppercase_symbols = any(symbol in string.ascii_uppercase
                                for symbol in password)
    has_digit_symbols = any(symbol in string.digits
                            for symbol in password)
    has_special_symbols = any(symbol in string.punctuation
                              for symbol in password)
    score = sum([has_lowercase_symbols, has_uppercase_symbols,
                 has_digit_symbols, has_special_symbols]) * 2.5
    if min_length_bound <= len(password) < max_lenght_bound:
        score -= 2
        return score
    else:
        return score


if __name__ == '__main__':
    password = getpass.getpass()
    filepath = input('Enter path: ')
    print('Password strength: {0}'.format(
        str(get_password_strength(password, load_blacklist(filepath)))))
