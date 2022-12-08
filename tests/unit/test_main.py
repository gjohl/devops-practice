import pytest

from devopspractice.main import greeting


@pytest.mark.parametrize("test_input,expected", [("Gurp", "Hello, Gurp"), ("Til", "Hello, Til"), ("Gurpreet Hisarli", "Hello, Gurpreet Hisarli")])
def test_greeting(test_input, expected):
    assert greeting(test_input) == expected

