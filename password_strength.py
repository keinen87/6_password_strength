import getpass
import os
import string


def load_blacklist_file(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as textfile:
        blacklist = [line.strip() for line in textfile]
    return blacklist 


def check_password(password, blacklist):
    if password in blacklist:
        return True


def check_password_on_lowercase(password):
    return any(symbol in string.ascii_lowercase for symbol in password)


def check_password_on_uppercase(password):
    return any(symbol in string.ascii_uppercase for symbol in password)


def check_password_on_digit_symbols(password):
    return any(symbol in string.digits for symbol in password)


def check_password_on_special_symbols(password):
    return any(symbol in string.punctuation for symbol in password)


def get_password_strength(password):
    score = 0
    min_length_bound = 5
    max_lenght_bound = 8
    if check_password(password, load_blacklist_file(filepath)) or \
            len(password) < min_length_bound:
        return score
    score = sum([check_password_on_lowercase(password),
                 check_password_on_uppercase(password),
                 check_password_on_digit_symbols(password),
                 check_password_on_special_symbols(password)
                 ]) * 2.5
    if min_length_bound <= len(password) < max_lenght_bound:
        score -= 2
    return score


if __name__ == '__main__':
    password = getpass.getpass()
    filepath = input('Enter path: ')
    print('Password strength: {0}'.format(
        str(get_password_strength(password))))
