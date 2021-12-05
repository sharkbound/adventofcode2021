import typing

from icecream import ic


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

    # iterators return themselves if you call iter() on it, this is to ensure it's a iterator
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
