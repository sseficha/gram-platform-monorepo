"""Hello unit test module."""

from orchestrator.hello import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello orchestrator"
