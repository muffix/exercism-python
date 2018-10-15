from collections.abc import Iterable


def _gen_flat(iterable):
    for item in iterable:
        if item is None:
            continue

        if isinstance(item, str):
            yield item
        elif isinstance(item, Iterable):
            yield from flatten(item)
        else:
            yield item


def flatten(iterable):
    return list(_gen_flat(iterable))
