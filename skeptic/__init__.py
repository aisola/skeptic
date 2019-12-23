
from .query import Query

select = Query.select
insert = Query.insert
update = Query.update
delete = Query.delete

__all__ = [
    'select',
    'insert',
    'update',
    'delete',
]
