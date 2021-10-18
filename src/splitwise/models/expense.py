from abc import ABC, abstractmethod
from .user import User
from .split import EqualSplit, ExactSplit, PercentageSplit, Split
from typing import List


class Expense(ABC):
    def __init__(self, title: str, amount: float, paid_by: User, splits: List[Split]) -> None:
        self.title = title
        self.amount = amount
        self.paid_by = paid_by
        self.splits = splits

    @abstractmethod
    def validate(self) -> bool:
        pass


class EqualExpense(Expense):
    def __init__(self, title: str, amount: float, paid_by: User, splits: List[Split]) -> None:
        super().__init__(title, amount, paid_by, splits)

    def validate(self) -> bool:
        for split in self.splits:
            if not isinstance(split, EqualSplit):
                return False
        return True


class ExactExpense(Expense):
    def __init__(self, title: str, amount: float, paid_by: User, splits: List[Split]) -> None:
        super().__init__(title, amount, paid_by, splits)

    def validate(self) -> bool:
        splits_amount = 0
        for split in self.splits:
            if not isinstance(split, ExactSplit):
                return False
            splits_amount += split.amount

        if splits_amount != self.amount:
            return False

        return True


class PercentageExpense(Expense):
    def __init__(self, title: str, amount: float, paid_by: User, splits: List[Split]) -> None:
        super().__init__(title, amount, paid_by, splits)

    def validate(self) -> bool:
        splits_percentage = 0
        for split in self.splits:
            if not isinstance(split, PercentageSplit):
                return False
            splits_percentage += split.percentage

        if splits_percentage != 100:
            return False

        return True
