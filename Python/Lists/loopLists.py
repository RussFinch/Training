# ======================= Play around with Python a bit (Optional Task 3) ============================
#        
#        Create a new file in this folder called loopLists.py.
#        Inside it, define a list of Strings of your 5 favourite movies.
#        Now, loop over the list. For each item in the list, print out "Movie: " plus the movies name.
#        Can you figure out how to print out Movie 1: <Movie 1's name>.
#        Movie 2: ... etc?
#        HINT: YOU WILL NEED TO LOOK UP the 'enumerate' command in Python using a Google search.
#        This command allows you to loop over a list retaining both the item at every position, and its index (i.e. position in the list).
#
# ==================================================================================================

favMovies = ['Batman', 'Superman', 'Ironman', 'Hulk', 'Thor']
numFavMovies = list(enumerate(favMovies, start=1))

for movies in numFavMovies:
    number = movies[0]
    name = movies[1]
    print("Movie " + str(number) + "'s name: " + str(name))