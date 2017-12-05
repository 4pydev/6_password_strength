import argparse
from getpass import getpass


def load_blacklist(blacklist_file):
    try:
        with open(blacklist_file, 'r') as file:
            return [bad_pass.strip() for bad_pass in file.readlines()]
    except FileNotFoundError:
        print("Specified blacklist file and/or \n"
              "default blacklist file doesn't exist.\n"
              "Blacklist test wasn't be performed.")
        return []


def get_password_strength(password, black_list):

    PASS_FEATURES_WEIGHTS = {
        'has_case_sensitivity': 1,
        'has_digits': 2,
        'has_special_chars': 2,
        'not_in_blacklist': 4
    }

    # initial password strength
    password_strength = 1

    if has_case_sensitivity(password):
        password_strength += PASS_FEATURES_WEIGHTS['has_case_sensitivity']

    if has_digits(password):
        password_strength += PASS_FEATURES_WEIGHTS['has_digits']

    if has_special_chars(password):
        password_strength += PASS_FEATURES_WEIGHTS['has_special_chars']

    if not is_in_blacklist(password, black_list):
        password_strength += PASS_FEATURES_WEIGHTS['not_in_blacklist']

    return password_strength


def has_case_sensitivity(password):
    return True if any(char.islower() for char in password) and \
                   any(char.isupper() for char in password) else False


def has_digits(password):
    return True if any(char.isdigit() for char in password) else False


def has_special_chars(password):
    return True if not password.isalnum() else False


def is_in_blacklist(password, black_list):
    if black_list == []:
        return True
    else:
        for word in black_list:
            if word.lower() == password.lower():
                return True
        return False


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--blacklist', default='./blacklist.txt')
    args = parser.parse_args()

    usr_password = getpass("Enter a password: ")
    print("Your password's strength: {}".format(
                    get_password_strength(usr_password,
                                          load_blacklist(args.blacklist))))
