import pytest


def test_set_compare():
    a = {'a', 'b'}
    b = {'b', 'a'}
    assert a == b


@pytest.mark.parametrize(
    ["a", "b", "result"],
    [
        [1, 2, 3],
        [2, 3, 5],
        [5, 3, 8],
    ],
)
def test_add_params(a, b, result):
    assert a + b == result


# https://docs.pytest.org/en/stable/how-to/fixtures.html#requesting-fixtures

# Arrange = GIVEN
@pytest.fixture
def first_entry():
    return "a"


# Arrange = GIVEN
@pytest.fixture
def second_entry():
    return 2


# Arrange = GIVEN
@pytest.fixture
def order(first_entry, second_entry):
    return [first_entry, second_entry]


# Arrange = GIVEN
@pytest.fixture
def expected_list():
    return ["a", 2, 3.0]


def test_string(order, expected_list):
    # Act = WHEN
    order.append(3.0)

    # Assert = THEN
    assert order == expected_list
