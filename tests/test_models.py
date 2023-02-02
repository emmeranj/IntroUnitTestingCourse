import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean


def test_everything_works():
    npt.assert_array_equal(np.array([0, 0]), np.array([0, 0]))







def test_daily_min_nonsense():
    from inflammation.models import daily_min
    from pytest import raises

    with raises(TypeError):
        daily_min('qwefegrg')


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0,0], [0,0], [0,0]], [0,0]),
        ([[1,2], [3,4], [5,6]], [3,4]),
    ])
def test_daily_mean(test, expected):
    from inflammation.models import daily_mean
    npt.assert_array_equal(np.array(expected), daily_mean(np.array(test)))

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0,0], [0,0], [0,0]], [0,0]),
        ([[1,2], [3,4], [5,6]], [1,2]),
    ])
def test_daily_min(test, expected):
    from inflammation.models import daily_min
    npt.assert_array_equal(np.array(expected), daily_min(np.array(test)))



@pytest.mark.parametrize(
    "test, error",
    [
        ([['Cannot', 'min'], ['string', 'arguments']], TypeError),
        ('qwefegrg', TypeError),
    ])
def test_daily_min_string(test, error):
    from inflammation.models import daily_min
    from pytest import raises
    with raises(error):
        daily_min(test)