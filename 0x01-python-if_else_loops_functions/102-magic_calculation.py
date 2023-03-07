#!/usr/bin/python3
# 102-magic_calculation.py
# Festus Maithya


def magic_calculation(a, b, c):
    """Match bytecode provided by ALX School."""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
