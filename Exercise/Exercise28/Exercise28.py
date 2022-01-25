# Exercise 28
# ------------------------------------------------------------------------------

movie = {
    'title': 'The Godfather',
    'director': 'Francis Ford Coppola',
    'year': 1972,
    'rating': 9.2,
}

movie['rating'] = (movie['rating'] + 9.3)/2

movie = {}
movie['title'] = 'The Godfather'
movie['director'] = 'Francis Ford Coppola'
movie['year'] = 1972
movie['rating'] = 9.2
print(movie)

movie['actors'] = ['Marlon Brando', 'Al Pacino', 'James Caan']
movie['other_details'] = {
    'runtime': 175,
    'language': 'English'
}
print(movie['other_details'])
