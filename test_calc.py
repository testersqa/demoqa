from calc import summary
import pytest


def test_summary_1():
    assert summary(2, 3) == 5

def test_summary_2():
    assert summary(2, 3) == 6