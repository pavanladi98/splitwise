from enum import Enum


class ExpenseType(Enum):
    """expense types"""
    Equal = "Equal"
    Percentage = "Percentage"
    Exact = "Exact"
