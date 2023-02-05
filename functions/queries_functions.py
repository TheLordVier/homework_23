from typing import Iterable


def filter_query(value: str, data: Iterable[str]):
    """
    Функция фильтрации запроса (входных данных)
    """
    return filter(lambda x: value in x, data)


def unique_query(data, *args, **kwargs):
    """
    Функция уникализации запроса
    """
    return set(data)


def limit_query(value, data):
    """
    Функция установки лимита на вывод данных
    """
    limit: int = int(value)
    return list(data)[:limit]


def map_query(value, data):
    """
    Функция деления исходных данных
    на колонки по пробелу
    """
    col_number = int(value)
    return map(lambda x: x.split(" ")[col_number], data)


def sorted_query(value, data):
    """
    Функция сортировки данных по возрастанию
    или убыванию
    """
    reverse = value == "desc"
    return sorted(data, reverse=reverse)
