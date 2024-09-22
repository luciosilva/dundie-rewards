"""Tests configuration."""

from functools import wraps


def bold(f):
    """Set bold style."""
    @wraps(f)
    def wrapper(text):
        return f(f"<strong>{text}</strong>")

    return wrapper


def italic(f):
    """Set italic style."""
    @wraps(f)
    def wrapper(text):
        return f(f"<i>{text}</i>")

    return wrapper


@bold
@italic
def hello(text):
    """Hello decorator example."""
    return f"Hello {text}"


print(hello("Fúria indepente"))
