
import pytest

from skeptic import select, insert, update, delete


statements = [
    (select, 'select'),
    (insert, 'insert'),
    (update, 'update'),
    (delete, 'delete'),
]


@pytest.mark.parametrize('statement_func,expected', statements)
def test_statement_kinds(statement_func, expected):
    query = statement_func('testing_table')
    assert query._stmt == expected, f'unexpected Query.stmt, expected={expected}, got={query._stmt}'
    assert query._table == 'testing_table', f'unexpected Query.table, expected=\'testing_table\', got={query._table}'
