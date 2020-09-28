import pytest
from example import get_hotp


@pytest.mark.parametrize("secret_bytes,counter,expected",
    [
        (b"12345678901234567890", 0, "755224"),
        (b"12345678901234567890", 1, "287082"),
        (b"12345678901234567890", 2, "359152"),
        (b"12345678901234567890", 3, "969429"),
        (b"12345678901234567890", 4, "338314"),
        (b"12345678901234567890", 5, "254676"),
        (b"12345678901234567890", 6, "287922"),
        (b"12345678901234567890", 7, "162583"),
        (b"12345678901234567890", 8, "399871"),
        (b"12345678901234567890", 9, "520489"),
        (b"12345678901234567890", 30, "026920"),
    ]
)
def test_get_hotp(secret_bytes, counter, expected):
    # Refer to https://tools.ietf.org/html/rfc4226
    actual = get_hotp(secret_bytes, counter)
    assert actual == expected
