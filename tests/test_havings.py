
import pytest

from skeptic.query import Query, Having


# having_tests defines a list of tuples for a table-test of the queries where capabilities. All this does is allows us
# to write these tests without redoing all of the boiler plate. Unfortunately, this also means that we have less
# descriptive names for our tests when they do fail. However, to combat that, we pass in an argvalue with a name.
having_tests = [
    (
        'having_eq',
        Query.select('test').having_eq('email', 'me@example.com'),
        Query(_stmt='select', _table='test', _havings=[Having(col="email", op="=", val=None)], _args=['me@example.com'])
    ),
    (
        'having_eq_raw',
        Query.select('test').having_eq_raw('email', 'me@example.com'),
        Query(_stmt='select', _table='test', _havings=[Having(col="email", op="=", val='me@example.com')])
    ),
    (
        'having_ne',
        Query.select('test').having_ne('email', 'me@example.com'),
        Query(_stmt='select', _table='test', _havings=[Having(col="email", op="!=", val=None)], _args=['me@example.com'])
    ),
    (
        'having_ne_raw',
        Query.select('test').having_ne_raw('email', 'me@example.com'),
        Query(_stmt='select', _table='test', _havings=[Having(col="email", op="!=", val='me@example.com')])
    ),
    (
        'having_gt',
        Query.select('test').having_gt('len', 10),
        Query(_stmt='select', _table='test', _havings=[Having(col="len", op=">", val=None)], _args=[10])
    ),
    (
        'having_gt_raw',
        Query.select('test').having_gt_raw('len', 10),
        Query(_stmt='select', _table='test', _havings=[Having(col="len", op=">", val=10)])
    ),
    (
        'having_gte',
        Query.select('test').having_gte('len', 10),
        Query(_stmt='select', _table='test', _havings=[Having(col="len", op=">=", val=None)], _args=[10])
    ),
    (
        'having_gte_raw',
        Query.select('test').having_gte_raw('len', 10),
        Query(_stmt='select', _table='test', _havings=[Having(col="len", op=">=", val=10)])
    ),
    (
        'having_lt',
        Query.select('test').having_lt('len', 10),
        Query(_stmt='select', _table='test', _havings=[Having(col="len", op="<", val=None)], _args=[10])
    ),
    (
        'having_lt_raw',
        Query.select('test').having_lt_raw('len', 10),
        Query(_stmt='select', _table='test', _havings=[Having(col="len", op="<", val=10)])
    ),
    (
        'having_lte',
        Query.select('test').having_lte('len', 10),
        Query(_stmt='select', _table='test', _havings=[Having(col="len", op="<=", val=None)], _args=[10])
    ),
    (
        'having_lte_raw',
        Query.select('test').having_lte_raw('len', 10),
        Query(_stmt='select', _table='test', _havings=[Having(col="len", op="<=", val=10)])
    ),
    (
        'having_in',
        Query.select('test').having_in('month', 'jan', 'feb'),
        Query(_stmt='select', _table='test', _havings=[Having(col='month', op='IN', val=None)], _args=['jan', 'feb'])
    ),
    (
        'having_in_none',
        Query.select('test').having_in('month'),
        Query(_stmt='select', _table='test')
    ),
    (
        'having_in_raw',
        Query.select('test').having_in_raw('month', 'jan', 'feb'),
        Query(_stmt='select', _table='test', _havings=[Having(col='month', op='IN', val='(jan, feb)')])
    ),
    (
        'having_in_raw_none',
        Query.select('test').having_in_raw('month'),
        Query(_stmt='select', _table='test')
    ),
    (
        'having_not_in',
        Query.select('test').having_not_in('month', 'jan', 'feb'),
        Query(_stmt='select', _table='test', _havings=[Having(col='month', op='NOT IN', val=None)], _args=['jan', 'feb'])
    ),
    (
        'having_not_in_none',
        Query.select('test').having_not_in('month'),
        Query(_stmt='select', _table='test')
    ),
    (
        'having_not_in_raw',
        Query.select('test').having_not_in_raw('month', 'jan', 'feb'),
        Query(_stmt='select', _table='test', _havings=[Having(col='month', op='NOT IN', val='(jan, feb)')])
    ),
    (
        'having_not_in_raw_none',
        Query.select('test').having_not_in_raw('month'),
        Query(_stmt='select', _table='test')
    ),
    (
        'having_like',
        Query.select('test').having_like('email', '%@example.com'),
        Query(_stmt='select', _table='test', _havings=[Having(col='email', op='LIKE', val=None)], _args=['%@example.com']),
    ),
    (
        'having_is_not_null',
        Query.select('test').having_is_not_null('email'),
        Query(_stmt='select', _table='test', _havings=[Having(col='email', op='IS NOT', val='NULL')]),
    ),
]


@pytest.mark.parametrize('testname,query,expected', having_tests)
def test_havings(testname, query, expected):
    assert query == expected
