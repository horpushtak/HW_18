from dao.model.movies import Movie


class MovieDAO:
    def __init__(self, session):  # Инициализируем с сессией, чтобы подключаться к БД
        self.session = session

    def get_movies(self, mid=None, **kwargs):  # По умолчанию None, чтобы была возможность выдать все
        query = self.session.query(Movie)

        if mid:
            return query.get(mid)  # Пусть сначала выдаст один фильм, а уж потом, если нужно, будет фильтровать

        if kwargs:
            for key, value in kwargs.items():
                query = query.filter(eval(f'Movie.{key}') == int(value))  # Вот опять, надо бы по-русски

        return query.all()

    def create(self, data):  # data здесь это словарь json
        new_movie = Movie(**data)
        with self.session.begin():
            self.session.add(new_movie)
        return new_movie  # Зачем?

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_movies(mid)
        self.session.delete(movie)
        self.session.commit()

# это файл для классов доступа к данным (Data Access Object).
# Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД
# Например
# class BookDAO:
#     def get_all_books(self):
#         books = Book.query.all()
#         return
