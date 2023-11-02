import pickle
from filmrec_constants import USERS_PICKLE_PATH, ADMIN_USER, ADMIN_PASSWORD


def get_users_data():
    with open(USERS_PICKLE_PATH, 'rb') as f:
        users_data = pickle.load(f)

    return users_data


def update_users_data(new_data):
    with open(USERS_PICKLE_PATH, 'wb') as f:
        pickle.dump(new_data, f)


def check_username(username, users_data):
    if username not in users_data:
        return False

    return True


def check_password(username, password, users_data):
    if password != users_data[username]:
        return False

    return True


def login(attempts, users_data):
    username = input('Please enter your user name: ')

    if username == ADMIN_USER:
        password = input('Please enter a password: ')
        return password == ADMIN_PASSWORD, username

    else:
        if not check_username(username, users_data):
            print('invalid username')
            return False, username

        for i in range(attempts):
            password = input('Please enter a password: ')

            if check_password(username, password, users_data):
                return True, username
            else:
                print('invalid password, try again')

        print('you ran out of attempts')
        return False, username


def add_username(new_username, new_password, users_data):
    users_data[new_username] = new_password
    update_users_data(users_data)


def remove_username(username, users_data):
    users_data.pop(username)
    update_users_data(users_data)
