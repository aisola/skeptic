
from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class Where:
    col: str
    op: str
    val: Any = None
    cat: str = ' AND '
    query: Any = None  # Should be type query, just dont know how to do that and too lazy to look it up.?


@dataclass
class Having:
    col: str
    op: str
    val: Any = None
    cat: str = ' AND '


@dataclass
class Set:
    col: str
    val: Any = None


@dataclass
class Order:
    cols: List[str] = None
    dir: str = None

    def is_zero(self):
        return self.cols is None and self.dir is None


@dataclass
class Query:
    _stmt: str
    _table: str
    _columns: List[str] = field(default_factory=list)
    _wheres: List[Where] = field(default_factory=list)
    _sets: List[Set] = field(default_factory=list)
    _group_by: List[str] = None
    _havings: List[Having] = field(default_factory=list)
    _order: Order = Order()
    _limit: int = None
    _offset: int = None
    _ret: List[str] = None
    _args: List[Any] = field(default_factory=list)

    @classmethod
    def select(cls, table):
        return Query(_stmt='select', _table=table)

    @classmethod
    def insert(cls, table):
        return Query(_stmt='insert', _table=table)

    @classmethod
    def update(cls, table):
        return Query(_stmt='update', _table=table)

    @classmethod
    def delete(cls, table):
        return Query(_stmt='delete', _table=table)

    def columns(self, *cols):
        self._columns = list(cols)
        return self

    def values(self, *vals):
        if self._stmt == 'insert':
            self._args = list(vals)
        return self

    def returning(self, *args):
        if self._stmt == 'insert' or self._stmt == 'update':
            self._ret = list(args)

        return self

    def limit(self, limit):
        self._limit = limit
        return self

    def offset(self, offset):
        self._offset = offset
        return self

    def group_by(self, *cols):
        if self._stmt == 'select':
            self._group_by = list(cols)
        return self

    def order_asc(self, *args):
        self._order.dir = 'asc'
        self._order.cols = list(args)
        return self

    def order_desc(self, *args):
        self._order.dir = 'desc'
        self._order.cols = list(args)
        return self

    def where_raw(self, col, *args):
        if len(args) == 1:
            op = '='
            val = args[0]
        else:
            op = args[0]
            val = args[1]

        if type(val) == list:
            val = '(' + ', '.join(val) + ')'

        self._wheres.append(Where(
            col=col,
            op=op,
            val=val,
        ))
        return self

    def or_where_raw(self, col, *args):
        if len(args) == 1:
            op = '='
            val = args[0]
        else:
            op = args[0]
            val = args[1]

        if type(val) == list:
            val = '(' + ', '.join(val) + ')'

        self._wheres.append(Where(
            col=col,
            op=op,
            val=val,
            cat=' OR ',
        ))
        return self

    def where(self, col, *args):
        if len(args) == 1:
            self.where_raw(col, None)
            val = args[0]
        else:
            self.where_raw(col, args[0], None)
            val = args[1]

        if type(val) == list:
            for arg in val:
                self._args.append(arg)
        else:
            self._args.append(val)

        return self

    def or_where(self, col, *args):
        if len(args) == 1:
            self.or_where_raw(col, None)
            val = args[0]
        else:
            self.or_where_raw(col, args[0], None)
            val = args[1]

        if type(val) == list:
            for arg in val:
                self._args.append(arg)
        else:
            self._args.append(val)

        return self

    def where_in_query(self, col, query):
        if query._is_zero():
            return self

        self._wheres.append(Where(col=col, op='IN', query=query))

        for arg in query._args:
            self._args.append(arg)

        return self

    def or_where_in_query(self, col, query):
        if query._is_zero():
            return self

        self._wheres.append(Where(col=col, op='IN', cat=' OR ', query=query))

        for arg in query._args:
            self._args.append(arg)

        return self

    def having_raw(self, col, *args):
        if len(args) == 1:
            op = '='
            val = args[0]
        else:
            op = args[0]
            val = args[1]

        if type(val) == list:
            val = '(' + ', '.join(val) + ')'

        self._havings.append(Having(
            col=col,
            op=op,
            val=val,
        ))
        return self

    def having(self, col, *args):
        if len(args) == 1:
            self.having_raw(col, None)
            val = args[0]
        else:
            self.having_raw(col, args[0], None)
            val = args[1]

        if type(val) == list:
            for arg in val:
                self._args.append(arg)
        else:
            self._args.append(val)

        return self

    def set_raw(self, col, val):
        if self._stmt != 'update':
            return self

        self._sets.append(Set(col=col, val=val))
        return self

    def set(self, col, val):
        if self._stmt != 'update':
            return self

        self.set_raw(col, None)
        self._args.append(val)
        return self

    def _is_zero(self):
        return (self._stmt == '' and
                self._table == '' and
                len(self._columns) == 0 and
                len(self._wheres) == 0 and
                len(self._sets) == 0 and
                self._order.is_zero() and
                self._limit == 0 and
                len(self._ret) == 0 and
                len(self._args) == 0)
