from __future__ import annotations

from functools import lru_cache
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
