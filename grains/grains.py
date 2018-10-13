from functools import wraps


def validate_square(f):
    @wraps(f)
    def decorator(square):
        if not 1 <= square <= 64:
            raise ValueError(f"Invalid square: {square}")
        return f(square)
    return decorator


@validate_square
def on_square(integer_number):
    return 1 << (integer_number-1)


@validate_square
def total_after(integer_number):
    return 2**integer_number-1
