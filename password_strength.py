import string
import sys

blacklist = ['qwerty','12345','123456','Password1','qwaszx','1q2w3e4r']


def get_password_strength(password):
    score = 0
    if password in blacklist:
        score += 1
        return score
    if password.isdigit():
        score += 2.5
        return score
    content = { 'has_lowercase_letters': True for symbol in password if symbol in string.ascii_lowercase }
    content.update({'has_uppercase_letters': True for symbol in password if symbol in string.ascii_uppercase })
    content.update({'has_digits': True for symbol in password if symbol in string.digits })
    content.update({'has_special_lettes': True for symbol in password if symbol in string.punctuation })
    score = 2.5 * len(content.values())
    return score


if __name__ == '__main__':
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print('Password strength: ' + str(get_password_strength(password)))
    else:
        print('Error! Enter password!')
