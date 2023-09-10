import pytest
from scale_calculator.tunings import get_all


def test_returns_not_empty_list():
    assert get_all() != []
