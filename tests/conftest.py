from decimal import Decimal
from faker import Faker
import pytest
from calculator.operations import add, subtract, multiply, divide

# Initialize Faker
fake = Faker()

# Define the operation mappings
operation_mappings = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

def generate_test_data(num_records):
    """Generates test data for arithmetic operations using Faker."""
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2))

        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        # Avoid division by zero
        if operation_func == divide and b == 0:
            b = Decimal('1')

        expected = operation_func(a, b)
        yield a, b, operation_name, expected

@pytest.fixture(params=list(generate_test_data(5)))
def operation_test_data(request):
    """Fixture for dynamically generated test data."""
    return request.param

@pytest.fixture
def calculator():
    """Fixture for creating a calculator instance."""
    from calculator import Calculator
    return Calculator()