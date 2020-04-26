import sys

try:
    x = 5
    y = 0
    result = x / y
except Exception:
    print('error thrown')

# With exception details
try:
    x = 5
    y = 0
    result = x / y
except ZeroDivisionError as e:
    print(f'{e!r}')


# Raise exceptions
try:
    raise ValueError("invalid value")
except ValueError as e:
    print(f'{e!r}')


# Re-raise an exception
try:
    x = 5
    y = 0
    result = x / y
except ZeroDivisionError as e:
    raise