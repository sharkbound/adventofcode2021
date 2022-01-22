import re
import typing
from typing import Callable, Any

__all__ = [
    'ITER_END_MARKER',
    'iter_with_terminator',
    'IterEndMarker',
    'iter_flatten',
    'get_all_ints',
    'build_dict',
    'first_where',
    'reverse_mapping',
    'format_map',
    'last_where',
]


class IterEndMarker:
    def __repr__(self):
        return '<IterEndMarker>'

    def __bool__(self):
        return False


ITER_END_MARKER = IterEndMarker()


def iter_with_terminator(iterable, end_marker=ITER_END_MARKER, include_end_marker=True, transform=None, predicate=None):
    if predicate is None:
        predicate = lambda x: True

    if transform is None:
        transform = lambda x: x

    # iterators return themselves if you call iter() on it, this is to ensure it's an iterator
    it = iter(iterable)

    while (value := next(it, end_marker)) != end_marker:
        if predicate(transformed := transform(value)):
            yield transformed

    if include_end_marker:
        yield end_marker


def iter_flatten(iterable, depth=None):
    if depth is not None and depth < 0:
        yield iterable
        return

    # strings and bytes are themselves iterable, so we dont want to include them
    if isinstance(iterable, typing.Iterable) and not isinstance(iterable, (str, bytes)):
        for x in iterable:
            yield from iter_flatten(x, depth=((depth - 1) if depth is not None else None))
    else:
        yield iterable


def get_all_ints(value, transform=iter):
    match value:
        case str() as s:
            return transform(map(int, re.findall(r'\d+', s)))
        case iterable if isinstance(iterable, typing.Iterable):
            return transform(map(int, iterable))
        case _:
            raise ValueError(f'cannot find ints from type: {type(value)}. value must be iterable!')


def build_dict(*items, cls=dict):
    """
    builds a dict from pairs passed, each 2 values are interpreted as (key, value)
    """
    # check that it's an even length
    assert len(items) & 1 != 1, 'length of items must be even in build_dict(...)'
    return cls(zip(items[::2], items[1::2]))


def first_where(iterable, predicate=lambda x: True, default=None):
    return next(filter(predicate, iterable), default)


def last_where(iterable, predicate=lambda x: True, default=None):
    val = default
    for item in filter(predicate, iterable):
        val = item
    return val


def reverse_mapping(mapping):
    return type(mapping)(zip(mapping.values(), mapping))


def format_map(items, format_: str | Callable, transform: Callable[[Any], Any] = None, args=False, kwargs=False):
    if not callable(format_):
        format_ = format_.format_map if kwargs else format_.format

    if transform is None:
        transform = lambda x: x

    if args:
        formatter = lambda x: format_(*x)
    else:
        formatter = format_

    return transform(map(formatter, items))
