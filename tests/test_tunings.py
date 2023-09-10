import pytest
from scale_calculator.tunings import get_all, get


def test_get_all_returns_not_empty_list():
    assert get_all() != []


all_tunings = [tuning.name for tuning in get_all()]


@pytest.mark.parametrize("name", all_tunings)
def test_get_returns_tuning_by_name(name):
    assert get(name).name == name
