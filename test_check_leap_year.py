"""A test module for the check_leap_year_module.
"""
from check_leap_year import is_leap_year

def test_positive():
    """A test for positive case."""
    assert is_leap_year(2016) is True

def test_negative():
    """A test for negative case."""
    assert is_leap_year(2010) is False

def test_centenary_positive():
    """A test for positive centenary case."""
    assert is_leap_year(2400) is True

def test_centenary_negative():
    """A test for negative centenary case."""
    assert is_leap_year(2100) is False
