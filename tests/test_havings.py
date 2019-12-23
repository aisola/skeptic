
import pytest

from skeptic.query import Query, Having


# having_tests defines a list of tuples for a table-test of the queries where capabilities. All this does is allows us
# to write these tests without redoing all of the boiler plate. Unfortunately, this also means that we have less
# descriptive names for our tests when they do fail. However, to combat that, we pass in an argvalue with a name.
having_tests = [
    (
        'having_eq',
        Query.select('test').having('email', 'me@example.com'),
        Query(_stmt='select', _table='test', _havings=[Having(col="email", op="=")], _args=['me@example.com'])
    ),
    (
        'having_eq_raw',
        Query.select('test').having_raw('email', 'me@example.com'),
        Query(_stmt='select', _table='test', _havings=[Having(col="email", op="=", val='me@example.com')])
    ),
    (
        'having_ne',
        Query.select('test').having('email', '!=', 'me@example.com'),
        Query(_stmt='select', _table='test', _havings=[Having(col="email", op="!=")], _args=['me@example.com'])
    ),
    (
        'having_ne_raw',
        Query.select('test').having_raw('email', '!=', 'me@example.com'),
        Query(_stmt='select', _table='test', _havings=[Having(col="email", op="!=", val='me@example.com')])
    ),
    (
        'having_gt',
        Query.select('test').having('len', '>', 10),
        Query(_stmt='select', _table='test', _havings=[Having(col="len", op=">", val=None)], _args=[10])
    ),
    (
        'having_gt_raw',
        Query.select('test').having_raw('len', '>', 10),
        Query(_stmt='select', _table='test', _havings=[Having(col="len", op=">", val=10)])
    ),
    (
        'having_gte',
        Query.select('test').having('len', '>=', 10),
        Query(_stmt='select', _table='test', _havings=[Having(col="len", op=">=", val=None)], _args=[10])
    ),
    (
        'having_gte_raw',
        Query.select('test').having_raw('len', '>=', 10),
        Query(_stmt='select', _table='test', _havings=[Having(col="len", op=">=", val=10)])
    ),
    (
        'having_lt',
        Query.select('test').having('len', '<', 10),
        Query(_stmt='select', _table='test', _havings=[Having(col="len", op="<", val=None)], _args=[10])
    ),
    (
        'having_lt_raw',
        Query.select('test').having_raw('len', '<', 10),
        Query(_stmt='select', _table='test', _havings=[Having(col="len", op="<", val=10)])
    ),
    (
        'having_lte',
        Query.select('test').having('len', '<=', 10),
        Query(_stmt='select', _table='test', _havings=[Having(col="len", op="<=", val=None)], _args=[10])
    ),
    (
        'having_lte_raw',
        Query.select('test').having_raw('len', '<=', 10),
        Query(_stmt='select', _table='test', _havings=[Having(col="len", op="<=", val=10)])
    ),
    (
        'having_in',
        Query.select('test').having('month', 'IN', ['jan', 'feb']),
        Query(_stmt='select', _table='test', _havings=[Having(col='month', op='IN', val=None)], _args=['jan', 'feb'])
    ),
    (
        'having_in_raw',
        Query.select('test').having_raw('month', 'IN', ['jan', 'feb']),
        Query(_stmt='select', _table='test', _havings=[Having(col='month', op='IN', val='(jan, feb)')])
    ),
    (
        'having_not_in',
        Query.select('test').having('month', 'NOT IN', ['jan', 'feb']),
        Query(_stmt='select', _table='test', _havings=[Having(col='month', op='NOT IN', val=None)], _args=['jan', 'feb'])
    ),
    (
        'having_not_in_raw',
        Query.select('test').having_raw('month', 'NOT IN', ['jan', 'feb']),
        Query(_stmt='select', _table='test', _havings=[Having(col='month', op='NOT IN', val='(jan, feb)')])
    ),
    (
        'having_like',
        Query.select('test').having('email', 'LIKE', '%@example.com'),
        Query(_stmt='select', _table='test', _havings=[Having(col='email', op='LIKE', val=None)], _args=['%@example.com']),
    ),
    (
        'having_like_raw',
        Query.select('test').having_raw('email', 'LIKE', '%@example.com'),
        Query(_stmt='select', _table='test', _havings=[Having(col='email', op='LIKE', val='%@example.com')]),
    ),
    (
        'having_is_not_null',
        Query.select('test').having_raw('email', 'IS NOT', 'NULL'),
        Query(_stmt='select', _table='test', _havings=[Having(col='email', op='IS NOT', val='NULL')]),
    ),
]


@pytest.mark.parametrize('testname,query,expected', having_tests)
def test_havings(testname, query, expected):
    assert query == expected
