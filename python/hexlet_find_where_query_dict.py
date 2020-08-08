"""
Реализуйте функцию find_where, которая принимает на вход список книг и поисковый запрос и возвращает первую книгу, 
которая соответствует запросу. Каждая книга в списке — это словарь, содержащий её параметры, 
поисковый запрос — тоже словарь с параметрами.

Если совпадений не было, то функция должна вернуть None.

books = [
     {'title': 'Book of Fooos', 'author': 'Foo', 'year': 1111},
     {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611},
     {'title': 'The Tempest', 'author': 'Shakespeare', 'year': 1611},
     {'title': 'Book of Foos Barrrs', 'author': 'FooBar', 'year': 2222},
     {'title': 'Still foooing', 'author': 'FooBar', 'year': 333},
     {'title': 'Happy Foo', 'author': 'FooBar', 'year': 4444},
 ]

>>find_where(books, {'author': 'Shakespeare', 'year': 1611})
{'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611}
"""

def find_where_old(books: dict, query: dict) -> set:
    #if query == {}:
    #    return books[0] ## not needed anymore 
    for book in books:
        for key in query:
            if key not in book.keys():
                break
            if query[key] != book[key]:
                break
        else:
            return book

def find_where(books: dict, query: dict) -> set:
    for book in books:
        for key, value in query.items:
            if key not in book.keys():
                break
            if value != book[key]:
                break
        else:
            return book

BOOKS = [
     {'title': 'Book of Fooos', 'author': 'Foo', 'year': 1111},
     {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611},
     {'title': 'The Tempest', 'author': 'Shakespeare', 'year': 1611},
     {'title': 'Book of Foos Barrrs', 'author': 'FooBar', 'year': 2222},
     {'title': 'Still foooing', 'author': 'FooBar', 'year': 333},
     {'title': 'Happy Foo', 'author': 'FooBar', 'year': 4444},
 ]

#print(find_where(BOOKS, {'author': 'Shakespeare', 'year': 1611}))
#print(find_where(BOOKS, {}))
#print(find_where(BOOKS, {'author': 'Pushkin'}))
#print(find_where(BOOKS, {'year': 1111, 'author': 'Pushkin'}))
#print(find_where(BOOKS, {'year': 1111}))
print(find_where(BOOKS, {"genre": 'Thriller'}))




def find_where_hexlet(items, search_request):
    # Значение object() в качестве умолчательного используется для того,
    # чтобы не получилось получить от get значение None и случайно
    # успешно сравнить с value == None.
    # Каждое значение object() всегда равно только самому себе.
    default = object()
    for item in items:
        for key, value in search_request.items():
            # Здесь можно было бы использовать
            # что-то вроде "key in book and book[key] !=..." и обойтись
            # без всяких object(). Но хочется обращаться по ключу
            # ровно один раз!
            if item.get(key, default) != value:
                break
        else:
            return item

#print(find_where_hexlet(BOOKS, {"genre": 'Thriller'}))