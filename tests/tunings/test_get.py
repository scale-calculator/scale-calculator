import string

import pytest
from hypothesis import assume, given
from hypothesis.strategies import text

from scale_calculator.tunings import UnknownTuningError, get, get_all

all_tunings = [tuning.name for tuning in get_all()]


@pytest.mark.parametrize("name", all_tunings)
def test_returns_tuning_by_name(name):
    assert get(name).name == name


@given(text(alphabet=string.ascii_letters + "_"))
def test_returns_error_when_not_know_tuning(unknown_tuning):
    assume(unknown_tuning not in all_tunings)
    with pytest.raises(UnknownTuningError):
        get(unknown_tuning)
