# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное,
# что требуется для приложения.
# этот файл часто является точкой входа в приложение

from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.directors.directors import directors_ns
from views.genres.genres import genres_ns
from views.movies.movies import movie_ns

# функция создания основного объекта app


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application


# def create_data(application, database):
  #  with application.app_context():
   #     database.create_all()

# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)


def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)  # импорты не видны
    # create_data(application, db)


app = create_app(Config())

if __name__ == '__main__':
    app.run()

#
#
# функция
# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#         создать несколько сущностей чтобы добавить их в БД
#
#         with db.session.begin():
#             db.session.add_all(здесь список созданных объектов)
#
#