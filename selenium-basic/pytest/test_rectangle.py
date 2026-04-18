import pytest

def calculate_rectangle(width, height):
    area = width * height
    return area

@pytest.mark.parametrize("width, height, expected_result", [(5, 15, 75), (10, 20, 200), (20, 30, 600), (25, 35, 875)])
def test_add_rectangle(width,height, expected_result):
    result = calculate_rectangle(width, height)
    print(result)
    assert result == expected_result

@pytest.fixture()
def setup():
    global num1, num2
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    yield
    print("\nOutput:", output)

def test_addition(setup):
    global output
    output = num1 + num2

def test_subtraction(setup):
    global output
    output = num1 - num2

def test_multiplication(setup):
    global output
    output = num1 * num2
