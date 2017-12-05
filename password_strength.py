from getpass import getpass


PASS_FEATURES_WEIGHTS = {
    'has_case_sensitivity': 1,
    'has_digits': 2,
    'has_special_chars': 2,
    'not_in_blacklist': 4
}
BLACKLIST = './blacklist.txt'


def load_blacklist(blacklist_file=BLACKLIST):
    try:
        with open(blacklist_file, 'r') as file:
            black_list = file.read().split()
        return black_list
    except FileNotFoundError:
        return []


def get_password_strength(password):
    # initial password strength
    password_strength = 1

    if has_case_sensitivity(password):
        password_strength += PASS_FEATURES_WEIGHTS['has_case_sensitivity']

    if has_digits(password):
        password_strength += PASS_FEATURES_WEIGHTS['has_digits']

    if has_special_chars(password):
        password_strength += PASS_FEATURES_WEIGHTS['has_special_chars']

    if not is_in_blacklist(password):
        password_strength += PASS_FEATURES_WEIGHTS['not_in_blacklist']
    return password_strength


def has_case_sensitivity(password):
    upper_chars = 0
    lower_chars = 0
    for char in password:
        upper_chars += 1 if char.isupper() else False
        lower_chars += 1 if char.islower() else False
    return bool(upper_chars > 0 and lower_chars > 0)


def has_digits(password):
    for char in password:
        if char.isdigit():
            return True
    return False


def has_special_chars(password):
    for char in password:
        if not char.isalpha() and not char.isdigit():
            return True
    return False


def is_in_blacklist(password, black_list=load_blacklist(BLACKLIST)):
    if black_list == []:
        return True
    else:
        for word in black_list:
            if word.lower() == password.lower():
                return True
        return False


if __name__ == '__main__':
    usr_password = getpass("Enter a password: ")
    print("Your password strength: {}".format(
                        get_password_strength(usr_password)))
