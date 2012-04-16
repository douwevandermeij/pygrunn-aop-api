from login import create_token


def test_token():
    assert create_token('aa', 'bb') == '1234567890'
