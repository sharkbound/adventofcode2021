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
        if predicate(value):
            yield transform(value)

    if include_end_marker:
        yield end_marker
