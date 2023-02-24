from __future__ import annotations

import time
from datetime import datetime
from datetime import timedelta
from functools import lru_cache
from functools import wraps
from textwrap import dedent


@lru_cache(maxsize=2)
def get_data(key):
    print('miss '+key)
    # A costly I/O usually implemented below
    return 'hit ' + key


def test_get_data(capsys):
    expected = dedent("""\
        miss 1
        hit 1
        miss 2
        hit 2
        hit 1
        miss 3
        hit 3
        hit 3
    """)
    print(get_data('1'))
    print(get_data('2'))
    print(get_data('1'))
    print(get_data('3'))
    print(get_data('3'))
    captured = capsys.readouterr()
    assert captured.out == expected


def timed_lru_cache(seconds: int, maxsize: int = 128):
    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache


@timed_lru_cache(seconds=1, maxsize=2)
def get_data_timed_cache(key):
    print('miss '+key)
    # A costly I/O usually implemented below
    return 'hit ' + key


def test_get_data_timed_cache(capsys):
    expected = dedent("""\
        miss 1
        hit 1
        miss 2
        hit 2
        hit 1
        miss 1
        hit 1
    """)
    print(get_data_timed_cache('1'))
    print(get_data_timed_cache('2'))
    print(get_data_timed_cache('1'))
    time.sleep(1)
    print(get_data_timed_cache('1'))
    captured = capsys.readouterr()
    assert captured.out == expected
