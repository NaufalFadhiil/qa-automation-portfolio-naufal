import pytest

def calculate_rectangle(width, height):
    area = width * height
    return area

def test_add_rectangle():
    result = calculate_rectangle(5, 15)
    assert result == 75
