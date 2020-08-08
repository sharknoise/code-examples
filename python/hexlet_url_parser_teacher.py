"""
Реализуйте абстракцию для работы с URL. Она должна извлекать и менять части адреса.
Все сеттеры должны возвращать новый изменённый URL, а старый оставлять неизменным
urlparse возвращает иммутабельный объект типа namedtuple. Получить копию такого объекта с одним изменённым значением можно с помощью метода _replace.
ParseResult(scheme='http', netloc='hexlet.io', path='/community', params='', query='q=low', fragment='')
"""
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse


def make(url):
    """Make an URL representation from string."""
    return urlparse(url)


def get_scheme(data):
    """Return a scheme of given URL."""
    return data.scheme


def set_scheme(data, scheme):
    """Return a new URL with replaced host."""
    return data._replace(scheme=scheme)  # noqa: WPS437


def get_host(data):
    """Return a host of given URL."""
    return data.netloc


def set_host(data, host):
    """Return a new URL with replaced host."""
    return data._replace(netloc=host)  # noqa: WPS437


def get_path(data):
    """Replace scheme of given URL."""
    return data.path


def set_path(data, path):
    """Return a new URL with replaced path."""
    return data._replace(path=path)  # noqa: WPS437


def get_query_param(data, key, default=None):
    """
    Return a value of named query parameter of given URL.

    Function returns default value if named parameter is not present.
    """
    return parse_qs(data.query).get(key, [default])[0]


def set_query_param(data, key, value):
    """Return a new URL with replaced query parameter."""
    params = parse_qs(data.query)
    if value is None:
        params.pop(key, None)
    else:
        params[key] = value
    return data._replace(query=urlencode(params, doseq=True))  # noqa: WPS437


def to_string(data):
    """Return a string representation of given URL."""
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