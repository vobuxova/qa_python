import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2
    
    @pytest.mark.parametrize('name', ['Г', 'Что делать, если ваш кот хочет вас убить'])    
    def test_add_new_book_genre_is_empty(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.books_genre[name] == ''
        
    @pytest.mark.parametrize('name, genre', [['Г', 'Ужасы'], ['Что делать, если ваш кот хочет вас убить', 'Комедии']])
    def test_set_book_genre_is_not_empty(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        print(type(collector))
        assert collector.books_genre[name] == genre
    
    @pytest.mark.parametrize('name, genre', [['Г', 'Ужасы'], ['Что делать, если ваш кот хочет вас убить', 'Комедии']])   
    def test_get_book_genre_appropriate_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre
        
    def test_get_books_with_specific_genre_books_with_this_genre_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби']
        
    def test_get_books_with_specific_genre_books_with_empty_genre_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert collector.get_books_with_specific_genre('') == []
        
    def test_get_books_genre_books_genre_is_not_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector.get_books_genre()
        assert collector.books_genre == {
            'Гордость и предубеждение и зомби': 'Ужасы',
            'Что делать, если ваш кот хочет вас убить': 'Комедии'
        }
        
    def test_get_books_for_children_book_for_children_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert collector.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить']
        
    def test_add_book_in_favorites_book_added_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.favorites == ['Гордость и предубеждение и зомби']
        
    def test_delete_book_from_favorites_book_is_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.favorites
        
    def test_get_list_of_favorites_books_favorites_is_not_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']