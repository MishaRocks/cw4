from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.movie import MovieDAO
from app.dao.user import UserDAO
from app.servises.director import DirectorService
from app.servises.genre import GenreService
from app.servises.movie import MovieService
from app.servises.user import UserService
from setup_db import db

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)
