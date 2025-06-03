"""Sample Hello World application."""

from contracts.foo import bar

from orchestrator.temp import x


def hello():
    """Return a friendly greeting."""
    print(f"Value of x: {x}")
    bar()
    return "Hello orchestrator"
