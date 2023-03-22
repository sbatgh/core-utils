from collections.abc import Mapping


def dot_notation(dict_: dict) -> object:
    """
    Converts a dictionary to an object that allows accessing keys using dot notation.
    """
    if isinstance(dict_, Mapping):
        return DotDict({k: dot_notation(v) for k, v in dict_.items()})
    else:
        return dict_


class DotDict(dict):
    """
    Allows accessing keys using dot notation.
    """
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
