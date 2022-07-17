from flask import request
from flask_restx import Resource, Namespace

from dao.model.movies import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    schema = MovieSchema(many=True)  # "Можно сделать атрибутом" атрибутом чего?

    def get(self):
        movies = self.schema.dump(movie_service.get_movies(**request.args))
        return movies, 200

    def post(self):
        new_movie = movie_service.create_movie(request.json)  # Сверху забираем то, что внизу будет data request-ом
        return "", 201, {'location': f'{movie_ns.path}/{new_movie}'}  # Так, что это вообще такое


@movie_ns.route('/<int:mid>')
class MoviesView(Resource):
    schema = MovieSchema()

    def get(self, mid: int):
        return self.schema.dump(movie_service.get_movies(mid)), 200

    def patch(self, mid: int):
        return self.schema.dump(movie_service.partial_update(mid, request.json)), 200  # request.json как data в MovieService

    def put(self, mid: int):
        return self.schema.dump(movie_service.full_update(mid, request.json)), 200

    def delete(self, mid: int):
        movie_service.delete_movie(mid)
        return "", 204
