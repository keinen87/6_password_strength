import argparse
import getpass
import string


def load_blacklist_file(filepath):
    with open(filepath, 'r') as textfile:
        blacklist = [line.strip() for line in textfile]
        return blacklist


def is_password_in_blacklist(password, blacklist):
    return password in blacklist


def is_password_in_lowercase(password):
    return any(symbol in string.ascii_lowercase for symbol in password)


def is_password_in_uppercase(password):
    return any(symbol in string.ascii_uppercase for symbol in password)


def is_password_in_digit_symbols(password):
    return any(symbol in string.digits for symbol in password)


def is_password_in_special_symbols(password):
    return any(symbol in string.punctuation for symbol in password)


def get_password_strength(password, blacklist):
    score = 0
    min_length_bound = 5
    max_lenght_bound = 8
    if blacklist or len(password) < min_length_bound:
        return score
    score = sum([is_password_on_lowercase(password),
                 is_password_on_uppercase(password),
                 is_password_on_digit_symbols(password),
                 is_password_on_special_symbols(password)
                 ]) * 2.5
    if min_length_bound <= len(password) < max_lenght_bound:
        score -= 2
    return score


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Path to file')
    args = parser.parse_args()
    filepath = args.filepath
    password = getpass.getpass()
    print('Password strength: {0}'.format(get_password_strength(
        password,
        is_password_in_blacklist(password, load_blacklist_file(filepath)))))
