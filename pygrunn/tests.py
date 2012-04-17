from pygrunn.core.login import create_token


def test_something():
    assert create_token('a', 'b') == '1234567890'
