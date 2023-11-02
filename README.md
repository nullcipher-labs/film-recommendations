# film-recommendations
A film recommendation system based on python, using collaborative filtering and cosine similarity.

# prerequisites
pandas, numpy

# python project
filmrec_main - contains the menus of the app, this is the file to run the entire app from
filmrec_constants - contains constants (file locations, menu texts)
filmrec_recommender - contains the Recommender class, which contains all the features of the reccomendation algorithms
filmrec_users - contains all the logic for users and passwords
filmerec_rating - contains all the logic for updating and adding ratings to the table

# files
in the data folder, you can find:
* admin_options.txt - text for the admin menu
* menu_options.txt - text for the normal user menu
* ratings.csv - table of film ratings by user
* users.pickle - dictionary of users and passwords
