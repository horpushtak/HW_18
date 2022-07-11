from dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_movies(self, mid=None, **kwargs):
        return self.dao.get_movies(mid, **kwargs)

    def create_movie(self, data):
        return self.dao.create(data)

    def full_update(self, mid, data):
        movie = self.get_movies(mid)

        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']
        self.dao.update(movie)
        return movie  # Мы поднимаем movie на уровень ...

    def partial_update(self, mid, data):
        movie = self.get_movies(mid)

        if 'title' in data:
            movie.title = data['title']
        elif 'description' in data:
            movie.description = data['description']
        elif 'trailer' in data:
            movie.trailer = data['trailer']
        elif 'year' in data:
            movie.year = data['year']
        elif 'rating' in data:
            movie.rating = data['rating']
        elif 'genre_id' in data:
            movie.genre_id = data['genre_id']
        elif 'director_id' in data:
            movie.director_id = data['director_id']
        self.dao.update(movie)
        return movie  # Мы поднимаем movie на уровень ...

    def delete_movie(self, mid):
        self.dao.delete(mid)

    def filter_movies_by_genre(self, gid):
        movies = self.get_movies()
        result = []
        for movie in movies:
            if movie.genre_id == int(gid):  # В базе это строчка
                result.append(movie)
        return result


