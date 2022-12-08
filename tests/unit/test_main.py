import pytest

from devopspractice.main import greeting


@pytest.mark.parametrize("test_input,expected", [("Gurp", "Hello, Gurp"), (None, "Hello, "), ("", 42)])
def test_greeting():
    actual = greeting("Gurp")
    expected = "Hello, Gurp"

    assert actual == expected
