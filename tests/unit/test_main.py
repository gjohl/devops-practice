import pytest

from devopspractice.main import greeting
from devopspractice.utils.exceptions import BadInputError


@pytest.mark.parametrize("test_input,expected", [("Gurp", "Hello, Gurp"), ("Til", "Hello, Til"),
                                                 ("Gurpreet Hisarli", "Hello, Gurpreet Hisarli")])
def test_greeting(test_input, expected):
    assert greeting(test_input) == expected


@pytest.mark.parametrize("test_input", [None, ""])
def test_greeting_raises(test_input):
    with pytest.raises(BadInputError, match="not be empty"):
        greeting(test_input)

