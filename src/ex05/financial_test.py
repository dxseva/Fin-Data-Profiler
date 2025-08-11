import pytest
import sys
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch

# Mock sys.argv to a safe value before importing financial
with patch('sys.argv', ['financial.py', 'MSFT', 'Total Revenue']):
    import financial

@pytest.fixture
def run_financial(request):
    """Fixture to run financial.py with specified sys.argv and capture output."""
    with patch('sys.argv', ['financial.py'] + list(request.param)):
        output = StringIO()
        try:
            with redirect_stdout(output):
                import importlib
                importlib.reload(financial)
        except Exception as e:
            return e  # return exception to test cases that expect it
        return eval(output.getvalue().strip())


@pytest.mark.parametrize("run_financial", [('MSFT', 'Total Revenue')], indirect=True)
def test_total_revenue_output(run_financial):
    """Test that financial.py returns correct Total Revenue for MSFT."""
    result = run_financial
    assert isinstance(result, tuple), "Output is not a tuple"
    assert result[0] == 'Total Revenue', "First element should be 'Total Revenue'"
    assert len(result) >= 2, "Not enough values in the output"
    for value in result[1:]:
        assert value.isdigit(), f"Value {value} is not a valid integer string"

    expected = ('Total Revenue', '245122000000', '211915000000', '198270000000', '168088000000')
    if len(result) == len(expected):
        assert result == expected, f"Expected {expected}, got {result}"

@pytest.mark.parametrize("run_financial", [('AAPL', 'Net Income Common Stockholders')], indirect=True)
def test_output_is_tuple(run_financial):
    """Test that financial.py returns a tuple for a valid input."""
    result = run_financial
    assert isinstance(result, tuple), "Output is not a tuple"
    assert len(result) >= 2, "Tuple should have at least field name and one value"
    assert result[0] == 'Net Income Common Stockholders', "First element should be the field name"

@pytest.mark.parametrize("run_financial", [('INVALIDTICKER', 'Total Revenue')], indirect=True)
def test_invalid_ticker_raises_exception(run_financial):
    """Test that financial.py raises an exception for an invalid ticker."""
    assert isinstance(run_financial, Exception), "Expected an Exception for invalid ticker"
    assert "Failed to fetch financial data" in str(run_financial) or \
           "No financial data found" in str(run_financial), \
           "Expected exception for invalid ticker"


@pytest.mark.parametrize("run_financial", [('MSFT', 'Nonexistent Field')], indirect=True)
def test_invalid_field_raises_exception(run_financial):
    """Test that financial.py raises an exception for an invalid field."""
    assert isinstance(run_financial, Exception), "Expected an Exception for invalid field"
    assert "Field 'Nonexistent Field' not found" in str(run_financial), \
           "Expected exception for invalid field"
