import sys


def get_password_strength(password):
    blacklist = ['qwerty','12345','123456','Password1','qwaszx','1q2w3e4r']
    low_case_letters, up_case_letters, numerical_digits, special_characters = False, False, False, False
    score = 0
    if password in blacklist:
        score += 1
        return score
    if password.isdigit():
        score = +2
        return score
    for symbol in password:
        if low_case_letters == False and 97 <= ord(symbol) <= 122:
            low_case_letters = True
        if up_case_letters == False and 65 <= ord(symbol) <= 90:
            up_case_letters = True
        elif numerical_digits == False and 48 <= ord(symbol) <= 57:
            numerical_digits = True
        elif special_characters == False and 33 <= ord(symbol) <= 47 or 58 <= ord(symbol) <= 64 or \
            91 <= ord(symbol) <= 96 or 123 <= ord(symbol) <= 126:
            special_characters = True
    if low_case_letters and up_case_letters and numerical_digits and special_characters:
        score = 10
        return score
    if low_case_letters:
        score += 2
    if up_case_letters:
        score += 3
    if numerical_digits:
        score += 3
    if special_characters:
        score += 3
    return score


if __name__ == '__main__':
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print('Password strength: ' + str(get_password_strength(password)))
    else:
        print('Error! Enter password!')
