from functools import wraps
from threading import Lock


def check_open(f):
    @wraps(f)
    def decorator(self, *args, **kwargs):
        if self.is_closed:
            print("Raising")
            raise ValueError("Account is closed")
        return f(self, *args, **kwargs)
    return decorator


def lock(f):
    def wrapped(self, *args, **kwargs):
        with self.lock:
            return f(self, *args, **kwargs)
    return wrapped


class BankAccount(object):
    def __init__(self):
        self.balance = 0
        self.is_closed = True
        self.lock = Lock()

    @check_open
    def get_balance(self):
        return self.balance

    def open(self):
        self.is_closed = False

    @lock
    @check_open
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    @lock
    @check_open
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Amount cannot be greater than balance")
        self.balance -= amount

    @lock
    @check_open
    def close(self):
        self.is_closed = True
        return self.balance
