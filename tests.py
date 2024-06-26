import pytest


class TestBooksCollector:

    # добавляем новую книгу
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['', 'Жизнь, необыкновенные и удивительные прик'])
    def test_add_new_book_add_books_len_name_not_in_books_genre(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_add_new_book_add_books_without_duplicate_books(self, collector):
        collector.add_new_book('Мор, ученик смерти')
        collector.add_new_book('Мор, ученик смерти')
        assert len(collector.books_genre) == 1

    # устанавливаем книге жанр
    def test_set_book_genre_add_book_and_set_genre(self, collector):
        collector.add_new_book('Понедельник начинается в субботу')
        collector.set_book_genre('Понедельник начинается в субботу', 'Фантастика')
        assert 'Фантастика' in collector.books_genre.values()

    def test_set_book_genre_add_book_and_set_non_existent_genre(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Роман')
        assert 'Роман' not in collector.books_genre.values()

    def test_set_book_genre_set_genre_not_add_book(self, collector):
        collector.set_book_genre('Сияние', 'Ужасы')
        assert 'Сияние' not in collector.books_genre

    # получаем жанр книги по её имени
    def test_get_book_genre_add_book_and_set_genre(self, collector):
        collector.add_new_book('Ревизор')
        collector.set_book_genre('Ревизор', 'Комедии')
        assert collector.books_genre.get('Ревизор') == 'Комедии'

    def test_get_book_genre_set_genre_without_add_book(self, collector):
        collector.set_book_genre('Ревизор', 'Комедии')
        assert collector.books_genre.get('Ревизор') is None

    # выводим список книг с определённым жанром
    def test_get_books_with_specific_genre_add_two_books_and_set_genre_displays_specific_genre(self, collector):
        collector.add_new_book('Рассказы о Шерлоке Холмсе')
        collector.add_new_book('Три кота')
        collector.set_book_genre('Рассказы о Шерлоке Холмсе', 'Детективы')
        collector.set_book_genre('Три кота', 'Мультфильмы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Рассказы о Шерлоке Холмсе']

    @pytest.mark.parametrize('genre', ['', 'Детективы'])
    def test_get_books_with_specific_genre_books_with_specific_genre_is_empty(self, collector, genre):
        collector.add_new_book('Рассказы о Шерлоке Холмсе')
        assert len(collector.get_books_with_specific_genre(genre)) == 0

    # получаем словарь books_genre

    def test_get_books_genre_add_two_books(self, collector):
        collector.add_new_book('Рассказы о Шерлоке Холмсе')
        collector.add_new_book('Три кота')
        assert collector.get_books_genre() == {'Рассказы о Шерлоке Холмсе': '', 'Три кота': ''}

    def test_get_books_genre_add_two_books_and_set_books_genre(self, collector):
        collector.add_new_book('Рассказы о Шерлоке Холмсе')
        collector.add_new_book('Три кота')
        collector.set_book_genre('Рассказы о Шерлоке Холмсе', 'Детективы')
        collector.set_book_genre('Три кота', 'Мультфильмы')
        assert collector.get_books_genre() == {'Рассказы о Шерлоке Холмсе': 'Детективы', 'Три кота': 'Мультфильмы'}

    def test_get_books_genre_books_genre_is_empty(self, collector):
        assert collector.get_books_genre() == {}

    # возвращаем книги, подходящие детям
    def test_get_books_for_children_add_two_books_set_children_genre(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Живая шляпа')
        collector.add_new_book('Этот неподражаемый Дживс')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Живая шляпа', 'Мультфильмы')
        collector.set_book_genre('Этот неподражаемый Дживс', 'Комедии')
        assert collector.get_books_for_children() == ['Гарри Поттер', 'Живая шляпа', 'Этот неподражаемый Дживс']

    @pytest.mark.parametrize(
        'books_and_genres',
        [
            [('Смерть на Ниле', 'Детективы'), ('Оно', 'Ужасы')],
            [],
            [('Смешарики', '')]
        ]
    )
    def test_get_books_for_children_books_for_children_is_empty(self, collector, books_and_genres):
        for book, genre in books_and_genres:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        assert collector.get_books_for_children() == []

    # добавляем книгу в Избранное
    def test_add_book_in_favorites_book_exists(self, collector):
        collector.add_new_book('Властелин Колец')
        collector.add_book_in_favorites('Властелин Колец')
        assert 'Властелин Колец' in collector.favorites

    def test_add_book_in_favorites_duplicate_book(self, collector):
        collector.add_new_book('Анна Каренина')
        collector.add_book_in_favorites('Анна Каренина')
        collector.add_book_in_favorites('Анна Каренина')
        assert collector.favorites.count('Анна Каренина') == 1

    # удаляем книгу из Избранного
    def test_delete_book_from_favorites_book_exists(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        collector.delete_book_from_favorites('Война и мир')
        assert 'Война и мир' not in collector.favorites

    def test_delete_book_from_favorites_book_not_exists(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        collector.delete_book_from_favorites('котики')
        assert 'Война и мир' in collector.favorites

    # получаем список Избранных книг
    def test_get_list_of_favorites_books_book_exists(self, collector):
        collector.add_new_book('Под знаком Мантикоры')
        collector.add_book_in_favorites('Под знаком Мантикоры')
        assert collector.get_list_of_favorites_books() == ['Под знаком Мантикоры']

    def test_get_list_of_favorites_books_is_empty(self, collector):
        assert collector.get_list_of_favorites_books() == []
