import pytest

from devopspractice.main import greeting, string_len
from devopspractice.utils.exceptions import BadInputError


@pytest.mark.parametrize("test_input,expected", [("Gurp", "Hello, Gurp"), ("Til", "Hello, Til"),
                                                 ("Gurpreet Hisarli", "Hello, Gurpreet Hisarli")])
def test_greeting(test_input, expected):
    assert greeting(test_input) == expected


@pytest.mark.parametrize("test_input,error_message", [(None, "not be empty"), ("", "not be empty"),
                                                      ("XO", "at least 3"), ("1", "at least 3")])
def test_greeting_raises(test_input, error_message):
    """Test that BadInputErrors are raised as expected."""
    with pytest.raises(BadInputError, match=error_message):
        greeting(test_input)


class TestStringLen:
    @staticmethod
    @pytest.mark.parametrize('input_string,expected', [('Gurp', 4), ('Tilman', 6)])
    def test_expected_result(input_string, expected):
        assert string_len(input_string) == expected

    @pytest.mark.parametrize('input_value', [1, 1., [], {'a': 1}])
    def test_raises(self, input_value):
        with pytest.raises(BadInputError, match="must be a string"):
            string_len(input_value)
