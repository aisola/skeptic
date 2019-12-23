
import pytest

from skeptic.query import Query, Order


columns_tests = [
    (['*'], ['*']),
    (['id', 'email', 'password'], ['id', 'email', 'password']),
]


@pytest.mark.parametrize('input,expected', columns_tests)
def test_columns(input, expected):
    expected = Query(_stmt='select', _table='test', _columns=expected)
    query = Query.select('test').columns(*input)
    assert expected == query


values_tests = [
    (Query.insert('test'), Query(_stmt='insert', _table='test', _args=['me@example.com', 23])),
    (Query.select('test'), Query(_stmt='select', _table='test')),
    (Query.update('test'), Query(_stmt='update', _table='test')),
    (Query.delete('test'), Query(_stmt='delete', _table='test')),
]


@pytest.mark.parametrize('query,expected', values_tests)
def test_values(query, expected):
    query = query.values('me@example.com', 23)
    assert query == expected


returning_tests = [
    (Query.insert, ['id', 'created_at'], 'insert', ['id', 'created_at']),
    (Query.update, ['id', 'created_at'], 'update', ['id', 'created_at']),
    (Query.select, ['id', 'created_at'], 'select', None),
]


@pytest.mark.parametrize('statement_func,returning,stmt,ret', returning_tests)
def test_returning(statement_func, returning, stmt, ret):
    expected = Query(_stmt=stmt, _table='test', _ret=ret)
    query = statement_func('test').returning(*returning)
    assert query == expected


def test_limit():
    expected = Query(_stmt='select', _table='test', _limit=10)
    query = Query.select('test').limit(10)
    assert query == expected


def test_offset():
    expected = Query(_stmt='select', _table='test', _offset=10)
    query = Query.select('test').offset(10)
    assert query == expected


def test_group_by():
    expected = Query(_stmt='select', _table='test', _group_by=['name', 'city'])
    query = Query.select('test').group_by('name', 'city')
    assert query == expected


def test_order_asc():
    expected = Query(_stmt='select', _table='test', _order=Order(cols=['created_at', 'updated_at'], dir='asc'))
    query = Query.select('test').order_asc('created_at', 'updated_at')
    assert query == expected


def test_order_desc():
    expected = Query(_stmt='select', _table='test', _order=Order(cols=['created_at', 'updated_at'], dir='desc'))
    query = Query.select('test').order_desc('created_at', 'updated_at')
    assert query == expected
