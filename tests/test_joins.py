
from skeptic.query import Query, Join, On


def test_inner_join():
    expected = Query(_stmt='select', _table='test')
    expected._joins = [Join(_kind='inner', _table='test2', _ons=[On(left='test.id', op='=', right='test2.id')])]
    query = Query.select('test')
    query.join('test2').on('test.id', '=', 'test2.id')
    assert query == expected


def test_multiple_joins():
    expected = Query(_stmt='select', _table='test')
    expected._joins = [
        Join(_kind='inner', _table='test2', _ons=[On(left='test.id', op='=', right='test2.tid')]),
        Join(_kind='inner', _table='test3', _ons=[
            On(left='test.id', op='=', right='test3.tid'),
            On(left='test.date', op='=', right='test3.tdate'),
        ]),
    ]
    query = Query.select('test')
    query.join('test2').on('test.id', '=', 'test2.tid')
    query.join('test3').on('test.id', '=', 'test3.tid').on('test.date', '=', 'test3.tdate')
    assert query == expected


def test_left_outer_join():
    expected = Query(_stmt='select', _table='test')
    expected._joins = [Join(_kind='left_outer', _table='test2', _ons=[On(left='test.id', op='=', right='test2.id')])]
    query = Query.select('test')
    query.left_outer_join('test2').on('test.id', '=', 'test2.id')
    assert query == expected


def test_right_outer_join():
    expected = Query(_stmt='select', _table='test')
    expected._joins = [Join(_kind='right_outer', _table='test2', _ons=[On(left='test.id', op='=', right='test2.id')])]
    query = Query.select('test')
    query.right_outer_join('test2').on('test.id', '=', 'test2.id')
    assert query == expected


def test_full_outer_join():
    expected = Query(_stmt='select', _table='test')
    expected._joins = [Join(_kind='full_outer', _table='test2', _ons=[On(left='test.id', op='=', right='test2.id')])]
    query = Query.select('test')
    query.full_outer_join('test2').on('test.id', '=', 'test2.id')
    assert query == expected
