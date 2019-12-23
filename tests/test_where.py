
import pytest

from skeptic.query import Query, Where


# where_tests defines a list of tuples for a table-test of the queries where capabilities. All this does is allows us to
# write these tests without redoing all of the boiler plate. Unfortunately, this also means that we have less
# descriptive names for our tests when they do fail. However, to combat that, we pass in an argvalue with a name.
where_tests = [
    (
        'where_eq',
        Query.delete('test').where_eq('email', 'me@example.com'),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="email", op="=", val=None)], _args=['me@example.com'])
    ),
    (
        'where_eq_raw',
        Query.delete('test').where_eq_raw('email', 'me@example.com'),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="email", op="=", val='me@example.com')])
    ),
    (
        'where_ne',
        Query.delete('test').where_ne('email', 'me@example.com'),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="email", op="!=", val=None)], _args=['me@example.com'])
    ),
    (
        'where_ne_raw',
        Query.delete('test').where_ne_raw('email', 'me@example.com'),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="email", op="!=", val='me@example.com')])
    ),
    (
        'where_gt',
        Query.delete('test').where_gt('len', 10),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="len", op=">", val=None)], _args=[10])
    ),
    (
        'where_gt_raw',
        Query.delete('test').where_gt_raw('len', 10),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="len", op=">", val=10)])
    ),
    (
        'where_gte',
        Query.delete('test').where_gte('len', 10),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="len", op=">=", val=None)], _args=[10])
    ),
    (
        'where_gte_raw',
        Query.delete('test').where_gte_raw('len', 10),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="len", op=">=", val=10)])
    ),
    (
        'where_lt',
        Query.delete('test').where_lt('len', 10),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="len", op="<", val=None)], _args=[10])
    ),
    (
        'where_lt_raw',
        Query.delete('test').where_lt_raw('len', 10),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="len", op="<", val=10)])
    ),
    (
        'where_lte',
        Query.delete('test').where_lte('len', 10),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="len", op="<=", val=None)], _args=[10])
    ),
    (
        'where_lte_raw',
        Query.delete('test').where_lte_raw('len', 10),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="len", op="<=", val=10)])
    ),
    (
        'where_in',
        Query.delete('test').where_in('month', 'jan', 'feb'),
        Query(_stmt='delete', _table='test', _wheres=[Where(col='month', op='IN', val=None)], _args=['jan', 'feb'])
    ),
    (
        'where_in_none',
        Query.delete('test').where_in('month'),
        Query(_stmt='delete', _table='test')
    ),
    (
        'where_in_raw',
        Query.delete('test').where_in_raw('month', 'jan', 'feb'),
        Query(_stmt='delete', _table='test', _wheres=[Where(col='month', op='IN', val='(jan, feb)')])
    ),
    (
        'where_in_raw_none',
        Query.delete('test').where_in_raw('month'),
        Query(_stmt='delete', _table='test')
    ),
    (
        'where_not_in',
        Query.delete('test').where_not_in('month', 'jan', 'feb'),
        Query(_stmt='delete', _table='test', _wheres=[Where(col='month', op='NOT IN', val=None)], _args=['jan', 'feb'])
    ),
    (
        'where_not_in_none',
        Query.delete('test').where_not_in('month'),
        Query(_stmt='delete', _table='test')
    ),
    (
        'where_not_in_raw',
        Query.delete('test').where_not_in_raw('month', 'jan', 'feb'),
        Query(_stmt='delete', _table='test', _wheres=[Where(col='month', op='NOT IN', val='(jan, feb)')])
    ),
    (
        'where_not_in_raw_none',
        Query.delete('test').where_not_in_raw('month'),
        Query(_stmt='delete', _table='test')
    ),
    (
        'where_in_query',
        Query.update('test').where_in_query('name', Query.select('people')),
        Query(_stmt='update', _table='test', _wheres=[Where(col='name', op='IN', val=None, query=Query(_stmt='select', _table='people'))])
    ),
    (
        'where_like',
        Query.select('test').where_like('email', '%@example.com'),
        Query(_stmt='select', _table='test', _wheres=[Where(col='email', op='LIKE', val=None)], _args=['%@example.com']),
    ),
    (
        'where_is_not_null',
        Query.select('test').where_is_not_null('email'),
        Query(_stmt='select', _table='test', _wheres=[Where(col='email', op='IS NOT', val='NULL')]),
    ),
]


@pytest.mark.parametrize('testname,query,expected', where_tests)
def test_wheres(testname, query, expected):
    assert query == expected
