#!/usr/bin/python3
# 102-magic_calculation.py
# Tracy Wankio MArwa


def magic_calculation(a, b, c):
    """Match bytecode provided by Holberton School."""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
