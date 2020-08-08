"""
Реализуйте абстракцию для работы с URL. Она должна извлекать и менять части адреса.
Все сеттеры должны возвращать новый изменённый URL, а старый оставлять неизменным
urlparse возвращает иммутабельный объект типа namedtuple. Получить копию такого объекта с одним изменённым значением можно с помощью метода _replace.
ParseResult(scheme='http', netloc='hexlet.io', path='/community', params='', query='q=low', fragment='')
"""
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode


def make(url: str):
    """Конструктор. Создает URL."""
    return urlparse(url)


def get_scheme(data):
    """Селектор (геттер). Извлекает схему."""
    return data.scheme


def set_scheme(data, scheme):
    """Сеттер. Меняет схему."""
    return data._replace(scheme=scheme)


def get_host(data):
    """Геттер. Извлекает host."""
    return data.netloc


def set_host(data, host):
    """Сеттер. Меняет host."""
    return data._replace(netloc=host)


def get_path(data):
    """Геттер. Извлекает путь."""
    return data.path


def set_path(data, path):
    """Сеттер. Меняет путь."""
    return data._replace(path=path)


def get_query_param(data, param_name, default=None):
    """
    Геттер. Извлекает значение для параметра запроса.

    Третьим параметром функция принимает значение по умолчанию, 
    которое возвращается тогда, когда в запросе не было такого параметра.
    """
    query_data = parse_qs(data.query)
    query_param = query_data.get(param_name, default)
    if isinstance(query_param, list):
        query_param = query_param[0]
    return query_param


def set_query_param(data, key, value):
    """
    Сеттер. Устанавливает значение для параметра запроса. 
    
    Если передано значение None, то параметр отбрасывается.
    """
    query_data = parse_qs(data.query)
    if value is None and key not in query_data:
        return data
    if value is None:
        query_data.pop(key)
    else:
        query_data[key] = [str(value)]
    print('query_data=', query_data)
    return data._replace(query=urlencode(query_data, doseq=True))


def to_string(data):
    """Геттер. Преобразует URL в строковой вид."""
    return urlunparse(data)


u = make('https://hexlet.io/community?q=low')

u = set_scheme(u, 'http')
to_string(u)
#'http://hexlet.io/community?q=low'

u = set_path(u, '/404')
to_string(u)
#'http://hexlet.io/404?q=low'

get_query_param(u, 'q')
#'low'

u = set_query_param(u, 'page', 5)
to_string(u)
#'http://hexlet.io/404?q=low&page=5'

u = set_query_param(u, 'q', 'high')
to_string(u)
#'http://hexlet.io/404?q=high&page=5'

u = set_query_param(u, 'q', None)
to_string(u)
#'http://hexlet.io/404?page=5'