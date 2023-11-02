from filmrec_recommender import Recommender
from filmrec_users import get_users_data, login, add_username, remove_username
from filmerec_rating import get_rating_data, rate_film, add_film, remove_film
from filmrec_constants import ADMIN_USER, MENU_OPTIONS_PATH, ADMIN_OPTIONS_PATH


def menu(menu_options, username):
    while True:
        print(f'\n{menu_options}')
        choice = input()

        if choice == '1':
            recommendation = r.recommend_film(username)
            print(f'You should really watch the film {recommendation}!')
        elif choice == '2':
            most_similar = r.get_most_similar_user(username)
            print(f'The user who is most similar to you in taste is {most_similar}!')
        elif choice == '3':
            new_pass = input('Please enter your new password: ')
            add_username(username, new_pass, users_data)
        elif choice == '4':
            film = input('Please enter the name of the film: ')
            rating = int(input('Please enter your rating: '))
            rate_film(username, film, rating, ratings_df)
        elif choice == '5':
            film = input('Please enter the name of the film: ')
            rate_film(username, film, None, ratings_df)
        elif choice == '6':
            break


def admin_menu(admin_options):
    while True:
        print(f'\n{admin_options}')
        choice = input()

        if choice == '1':
            new_user = input('Please enter the new user name: ')
            new_pass = input('Please enter the new password: ')
            add_username(new_user, new_pass, users_data)
        elif choice == '2':
            new_user = input('Please enter the user name to remove: ')
            remove_username(new_user, users_data)
        elif choice == '3':
            user = input('Please enter a user name to change their password: ')
            new_pass = input('Please enter a new password: ')
            add_username(user, new_pass, users_data)
        elif choice == '4':
            new_film = input('Please enter the name of the new film: ')
            add_film(ratings_df, new_film)
        elif choice == '5':
            film = input('Please enter the name of the film you want to remove: ')
            remove_film(ratings_df, film)
        elif choice == '6':
            break


# loading relevant data
ratings_df = get_rating_data()
r = Recommender(ratings_df)
users_data = get_users_data()

with open(MENU_OPTIONS_PATH, 'r') as f:
    menu_options = f.read()

with open(ADMIN_OPTIONS_PATH, 'r') as f:
    admin_options = f.read()

# logging the user in
is_admin = False
login_successful, username = login(3, users_data)
if not login_successful:
    exit()

# menu
if username == ADMIN_USER:
    admin_menu(admin_options)
else:
    menu(menu_options, username)
