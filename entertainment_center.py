"""Create a list of Movie object, and write out movie page."""

from media import Movie
import fresh_tomatoes

movies = []
movies.append(Movie('Alien: Prometheus',
'https://images-na.ssl-images-amazon.com/images/M/MV5BMTY3NzIyNTA2NV5BMl5BanBnXkFtZTcwNzE2NjI4Nw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg',  # NOQA
'https://www.youtube.com/watch?v=34cEo0VhfGE'))
movies.append(Movie('Alien: Covenant',
'https://images-na.ssl-images-amazon.com/images/M/MV5BNzI5MzM3MzkxNF5BMl5BanBnXkFtZTgwOTkyMjI4MTI@._V1_SY1000_CR0,0,673,1000_AL_.jpg',  # NOQA
'https://www.youtube.com/watch?v=svnAD0TApb8'))
movies.append(Movie('Life',
'https://images-na.ssl-images-amazon.com/images/M/MV5BMzAwMmQxNTctYjVmYi00MDdlLWEzMWUtOTE5NTRiNDhhNjI2L2ltYWdlXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_SY1000_SX675_AL_.jpg',  #NOQA
'https://www.youtube.com/watch?v=LeLsJfGmY_Y'))
movies.append(Movie('Guardians of the Galaxy Vol. 2',
'https://images-na.ssl-images-amazon.com/images/M/MV5BMTg2MzI1MTg3OF5BMl5BanBnXkFtZTgwNTU3NDA2MTI@._V1_SY1000_CR0,0,674,1000_AL_.jpg',  # NOQA
'https://www.youtube.com/watch?v=4hdv_6gl4gk'))

fresh_tomatoes.open_movies_page(movies)