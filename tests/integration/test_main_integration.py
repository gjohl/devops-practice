import pytest

from devopspractice.main import greeting, string_len
from devopspractice.utils.exceptions import BadInputError


class TestLenGreeting:
    @pytest.mark.parametrize("test_input,expected", [("Gurp", 7+4), ("Tilman", 7+6)])
    def test_success(self, test_input, expected):
        """Testing length of greeting. Includes "Hello, ", thus adds 7 chars to input len"""
        assert string_len(greeting(test_input)) == expected

    @pytest.mark.parametrize("test_input,error_message", [("", "not be empty"), ("Ti", "at least 3")])
    def test_raises(self, test_input, error_message):
        with pytest.raises(BadInputError, match=error_message):
            string_len(greeting(test_input))


