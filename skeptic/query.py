
from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class Where:
    col: str
    op: str
    val: Any = None
    cat: str = " AND "
    query: Any = None  # Should be type query, just dont know how to do that and too lazy to look it up.?


@dataclass
class Having:
    col: str
    op: str
    val: Any = None
    cat: str = " AND "


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

    def where_eq_raw(self, col, val):
        self._wheres.append(Where(
            col=col,
            op='=',
            val=val,
        ))
        return self

    def where_eq(self, col, val):
        q = self.where_eq_raw(col, None)
        q._args.append(val)
        return q

    def where_ne_raw(self, col, val):
        self._wheres.append(Where(
            col=col,
            op='!=',
            val=val,
        ))
        return self

    def where_ne(self, col, val):
        q = self.where_ne_raw(col, None)
        q._args.append(val)
        return q

    def where_gt_raw(self, col, val):
        self._wheres.append(Where(
            col=col,
            op='>',
            val=val,
        ))
        return self

    def where_gt(self, col, val):
        q = self.where_gt_raw(col, None)
        q._args.append(val)
        return q

    def where_gte_raw(self, col, val):
        self._wheres.append(Where(
            col=col,
            op='>=',
            val=val,
        ))
        return self

    def where_gte(self, col, val):
        q = self.where_gte_raw(col, None)
        q._args.append(val)
        return q

    def where_lt_raw(self, col, val):
        self._wheres.append(Where(
            col=col,
            op='<',
            val=val,
        ))
        return self

    def where_lt(self, col, val):
        q = self.where_lt_raw(col, None)
        q._args.append(val)
        return q

    def where_lte_raw(self, col, val):
        self._wheres.append(Where(
            col=col,
            op='<=',
            val=val,
        ))
        return self

    def where_lte(self, col, val):
        q = self.where_lte_raw(col, None)
        q._args.append(val)
        return q

    def where_in_raw(self, col, *vals):
        if len(vals) == 0:
            return self

        self._wheres.append(Where(
            col=col,
            op='IN',
            val='(' + ', '.join(vals) + ')',
        ))

        return self

    def where_in(self, col, *args):
        if len(args) == 0:
            return self

        self._wheres.append(Where(col=col, op='IN', val=None))

        for arg in args:
            self._args.append(arg)

        return self

    def where_not_in_raw(self, col, *vals):
        if len(vals) == 0:
            return self

        self._wheres.append(Where(
            col=col,
            op='NOT IN',
            val='(' + ', '.join(vals) + ')',
        ))

        return self

    def where_not_in(self, col, *args):
        if len(args) == 0:
            return self

        self._wheres.append(Where(col=col, op='NOT IN', val=None))

        for arg in args:
            self._args.append(arg)

        return self

    def where_in_query(self, col, query):
        if query._is_zero():
            return self

        self._wheres.append(Where(col=col, op='IN', val=None, query=query))

        for arg in query._args:
            self._args.append(arg)

        return self

    def where_like(self, col, like):
        self._wheres.append(Where(col=col, op='LIKE', val=None))
        self._args.append(like)
        return self

    def where_is_not_null(self, col):
        self._wheres.append(Where(col=col, op='IS NOT', val='NULL'))
        return self

    def having_eq_raw(self, col, val):
        self._havings.append(Having(
            col=col,
            op='=',
            val=val,
        ))
        return self

    def having_eq(self, col, val):
        q = self.having_eq_raw(col, None)
        q._args.append(val)
        return q

    def having_ne_raw(self, col, val):
        self._havings.append(Having(
            col=col,
            op='!=',
            val=val,
        ))
        return self

    def having_ne(self, col, val):
        q = self.having_ne_raw(col, None)
        q._args.append(val)
        return q

    def having_gt_raw(self, col, val):
        self._havings.append(Having(
            col=col,
            op='>',
            val=val,
        ))
        return self

    def having_gt(self, col, val):
        q = self.having_gt_raw(col, None)
        q._args.append(val)
        return q

    def having_gte_raw(self, col, val):
        self._havings.append(Having(
            col=col,
            op='>=',
            val=val,
        ))
        return self

    def having_gte(self, col, val):
        q = self.having_gte_raw(col, None)
        q._args.append(val)
        return q

    def having_lt_raw(self, col, val):
        self._havings.append(Having(
            col=col,
            op='<',
            val=val,
        ))
        return self

    def having_lt(self, col, val):
        q = self.having_lt_raw(col, None)
        q._args.append(val)
        return q

    def having_lte_raw(self, col, val):
        self._havings.append(Having(
            col=col,
            op='<=',
            val=val,
        ))
        return self

    def having_lte(self, col, val):
        q = self.having_lte_raw(col, None)
        q._args.append(val)
        return q

    def having_in_raw(self, col, *vals):
        if len(vals) == 0:
            return self

        self._havings.append(Having(
            col=col,
            op='IN',
            val='(' + ', '.join(vals) + ')',
        ))

        return self

    def having_in(self, col, *args):
        if len(args) == 0:
            return self

        self._havings.append(Having(col=col, op='IN', val=None))

        for arg in args:
            self._args.append(arg)

        return self

    def having_not_in_raw(self, col, *vals):
        if len(vals) == 0:
            return self

        self._havings.append(Having(
            col=col,
            op='NOT IN',
            val='(' + ', '.join(vals) + ')',
        ))

        return self

    def having_not_in(self, col, *args):
        if len(args) == 0:
            return self

        self._havings.append(Having(col=col, op='NOT IN', val=None))

        for arg in args:
            self._args.append(arg)

        return self

    def having_like(self, col, like):
        self._havings.append(Having(col=col, op='LIKE', val=None))
        self._args.append(like)
        return self

    def having_is_not_null(self, col):
        self._havings.append(Having(col=col, op='IS NOT', val='NULL'))
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
