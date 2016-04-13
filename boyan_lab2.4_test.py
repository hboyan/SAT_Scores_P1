# Dictionary of movies
movies = [
    {
    "name": "Usual Suspects",
    "imdb": 7.0,
    "category": "Thriller"
    },
    {
    "name": "Hitman",
    "imdb": 6.3,
    "category": "Action"
    },
    {
    "name": "Dark Knight",
    "imdb": 9.0,
    "category": "Adventure"
    },
    {
    "name": "The Help",
    "imdb": 8.0,
    "category": "Drama"
    },
    {
    "name": "The Choice",
    "imdb": 6.2,
    "category": "Romance"
    },
    {
    "name": "Colonia",
    "imdb": 7.4,
    "category": "Romance"
    },
    {
    "name": "Love",
    "imdb": 6.0,
    "category": "Romance"
    },
    {
    "name": "Bride Wars",
    "imdb": 5.4,
    "category": "Romance"
    },
    {
    "name": "AlphaJet",
    "imdb": 3.2,
    "category": "War"
    },
    {
    "name": "Ringing Crime",
    "imdb": 4.0,
    "category": "Crime"
    },
    {
    "name": "Joking muck",
    "imdb": 7.2,
    "category": "Comedy"
    },
    {
    "name": "What is the name",
    "imdb": 9.2,
    "category": "Suspense"
    },
    {
    "name": "Detective",
    "imdb": 7.0,
    "category": "Suspense"
    },
    {
    "name": "Exam",
    "imdb": 4.2,
    "category": "Thriller"
    },
    {
    "name": "We Two",
    "imdb": 7.2,
    "category": "Romance"
    }
    ]

# Write a function that takes a single movie and
# returns True if its IMDB score is above 5.5
def goodrate(movie):
    if movie['imdb'] > 5.5:
        return True

# Write a function that returns a sublist of movies
# with an IMDB score above 5.5.
def allgood(dict):
    goodMovies = []
    for movie in movies:
        if goodrate(movie):
            goodMovies.append(movie['name'])
    return goodMovies

# Write a function that takes a category name and returns
# just those movies under that category.
def inCat(cat):
    catMovies = []
    for movie in movies:
        if movie['category'] == cat:
            catMovies.append(movie)
    return catMovies

# Write a function that takes a list of movies and computes
# the average IMDB score.
def avgScore(list):
    total = 0
    count = 0
    for movie in list:
        total += movie['imdb']
        count += 1
    avg = total/count
    return avg

# Write a function that takes a category and computes
# the average IMDB score (HINT: reuse the function
# from question 2.)
def catScore(cat):
    movieList = inCat(cat)
    avg = avgScore(movieList)
    return avg

# Put it into action
def main():
    for movie in movies:
        print goodrate(movie)



main()
