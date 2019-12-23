
import pytest

from skeptic.query import Query, Where


# where_tests defines a list of tuples for a table-test of the queries where capabilities. All this does is allows us to
# write these tests without redoing all of the boiler plate. Unfortunately, this also means that we have less
# descriptive names for our tests when they do fail. However, to combat that, we pass in an argvalue with a name.
where_tests = [
    (
        'where_eq',
        Query.delete('test').where('email', 'me@example.com'),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="email", op="=")], _args=['me@example.com'])
    ),
    (
        'where_eq_raw',
        Query.delete('test').where_raw('email', 'me@example.com'),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="email", op="=", val='me@example.com')])
    ),
    (
        'where_ne',
        Query.delete('test').where('email', '!=', 'me@example.com'),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="email", op="!=")], _args=['me@example.com'])
    ),
    (
        'where_ne_raw',
        Query.delete('test').where_raw('email', '!=', 'me@example.com'),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="email", op="!=", val='me@example.com')])
    ),
    (
        'where_gt',
        Query.delete('test').where('len', '>', 10),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="len", op=">")], _args=[10])
    ),
    (
        'where_gt_raw',
        Query.delete('test').where_raw('len', '>', 10),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="len", op=">", val=10)])
    ),
    (
        'where_gte',
        Query.delete('test').where('len', '>=', 10),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="len", op=">=")], _args=[10])
    ),
    (
        'where_gte_raw',
        Query.delete('test').where_raw('len', '>=', 10),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="len", op=">=", val=10)])
    ),
    (
        'where_lt',
        Query.delete('test').where('len', '<', 10),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="len", op="<")], _args=[10])
    ),
    (
        'where_lt_raw',
        Query.delete('test').where_raw('len', '<', 10),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="len", op="<", val=10)])
    ),
    (
        'where_lte',
        Query.delete('test').where('len', '<=', 10),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="len", op="<=")], _args=[10])
    ),
    (
        'where_lte_raw',
        Query.delete('test').where_raw('len', '<=', 10),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="len", op="<=", val=10)])
    ),
    (
        'where_like',
        Query.select('test').where('email', 'LIKE', '%@example.com'),
        Query(_stmt='select', _table='test', _wheres=[Where(col='email', op='LIKE')], _args=['%@example.com']),
    ),
    (
        'where_like_raw',
        Query.select('test').where_raw('email', 'LIKE', '%@example.com'),
        Query(_stmt='select', _table='test', _wheres=[Where(col='email', op='LIKE', val='%@example.com')]),
    ),
    (
        'where_is_not_null',
        Query.select('test').where_raw('email', 'IS NOT', 'NULL'),
        Query(_stmt='select', _table='test', _wheres=[Where(col='email', op='IS NOT', val='NULL')]),
    ),
    (
        'where_in',
        Query.delete('test').where('month', 'IN', ['jan', 'feb']),
        Query(_stmt='delete', _table='test', _wheres=[Where(col='month', op='IN')], _args=['jan', 'feb'])
    ),
    (
        'where_in_raw',
        Query.delete('test').where_raw('month', 'IN', ['jan', 'feb']),
        Query(_stmt='delete', _table='test', _wheres=[Where(col='month', op='IN', val='(jan, feb)')])
    ),
    (
        'where_not_in',
        Query.delete('test').where('month', 'NOT IN', ['jan', 'feb']),
        Query(_stmt='delete', _table='test', _wheres=[Where(col='month', op='NOT IN')], _args=['jan', 'feb'])
    ),
    (
        'where_not_in_raw',
        Query.delete('test').where_raw('month', 'NOT IN', ['jan', 'feb']),
        Query(_stmt='delete', _table='test', _wheres=[Where(col='month', op='NOT IN', val='(jan, feb)')])
    ),
    (
        'where_in_query',
        Query.update('test').where_in_query('name', Query.select('people')),
        Query(_stmt='update', _table='test', _wheres=[Where(col='name', op='IN', query=Query(_stmt='select', _table='people'))])
    ),
    (
        'or_where_eq',
        Query.delete('test').or_where('email', 'me@example.com'),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="email", op="=", cat=' OR ')], _args=['me@example.com'])
    ),
    (
        'or_where_eq_raw',
        Query.delete('test').or_where_raw('email', 'me@example.com'),
        Query(_stmt='delete', _table='test', _wheres=[Where(col="email", op="=", cat=' OR ', val='me@example.com')])
    ),
    (
        'or_where_in',
        Query.delete('test').or_where('month', 'IN', ['jan', 'feb']),
        Query(_stmt='delete', _table='test', _wheres=[Where(col='month', op='IN', cat=' OR ')], _args=['jan', 'feb'])
    ),
    (
        'or_where_in_raw',
        Query.delete('test').or_where_raw('month', 'IN', ['jan', 'feb']),
        Query(_stmt='delete', _table='test', _wheres=[Where(col='month', op='IN', cat=' OR ', val='(jan, feb)')])
    ),
    (
        'or_where_in_query',
        Query.update('test').or_where_in_query('name', Query.select('people')),
        Query(_stmt='update', _table='test', _wheres=[Where(col='name', op='IN', cat=' OR ', query=Query(_stmt='select', _table='people'))])
    ),
]


@pytest.mark.parametrize('testname,query,expected', where_tests)
def test_wheres(testname, query, expected):
    assert query == expected
