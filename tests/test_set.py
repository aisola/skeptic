
from skeptic.query import Query, Set


def test_set():
    expected = Query(_stmt='update', _table='test', _sets=[Set(col='username', val=None)], _args=['me'])
    query = Query.update('test').set('username', 'me')
    assert query == expected


def test_set_multiple():
    expected = Query(_stmt='update', _table='test',
                     _sets=[Set(col='username', val=None), Set(col='password', val=None)],
                     _args=['me', 'you'])
    query = Query.update('test').set('username', 'me').set('password', 'you')
    assert query == expected


def test_set_not_update():
    expected = Query(_stmt='select', _table='test')
    query = Query.select('test').set('username', 'me')
    assert query == expected


def test_set_raw():
    expected = Query(_stmt='update', _table='test', _sets=[Set(col='username', val='me')])
    query = Query.update('test').set_raw('username', 'me')
    assert query == expected


def test_set_raw_multiple():
    expected = Query(_stmt='update', _table='test',
                     _sets=[Set(col='username', val='me'), Set(col='password', val='you')])
    query = Query.update('test').set_raw('username', 'me').set_raw('password', 'you')
    assert query == expected


def test_set_raw_not_update():
    expected = Query(_stmt='select', _table='test')
    query = Query.select('test').set_raw('username', 'me')
    assert query == expected