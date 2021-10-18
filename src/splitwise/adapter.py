from .models import User, Expense, Split, ExpenseType
from .models.expense import ExactExpense, EqualExpense, PercentageExpense
from .models.split import ExactSplit, PercentageSplit, EqualSplit
from .expense_service import ExpenseService
from typing import List


def adapt_user(request: dict) -> User:
    return User(
        id=request.get('Id'),
        name=request.get('Name'),
        phone=request.get('Phone'),
        email=request.get('Email'))


def get_user(user_id) -> User:
    return ExpenseService.get_user(user_id)


def generate_expense(title: str, expense_type: ExpenseType, amount: float, paid_by: User, splits: List[Split]):
    if expense_type == ExpenseType.Exact:
        return ExactExpense(title, amount, paid_by, splits)

    elif expense_type == ExpenseType.Percentage:
        return PercentageExpense(title, amount, paid_by, splits)

    elif expense_type == ExpenseType.Equal:
        return EqualExpense(title, amount, paid_by, splits)

    return None


def adapt_expense(request: dict) -> Expense:
    title = request.get('Title')
    total_amount = request.get('Amount')
    paid_by = get_user(request.get('PaidBy'))
    split_to = request.get('SplitTo')
    total_splits = len(split_to)
    expense_type = ExpenseType(request.get('ExpenseType'))
    splits = []
    for _split in split_to:
        user_id = _split.get('UserId')
        if expense_type == ExpenseType.Exact:
            amount = _split.get('Amount')
            split = ExactSplit(user=get_user(user_id), amount=amount)
        elif expense_type == ExpenseType.Equal:
            split = EqualSplit(user=get_user(user_id))
            split.amount = total_amount / total_splits
        elif expense_type == ExpenseType.Percentage:
            split = PercentageSplit(user=get_user(
                user_id), percentage=_split.get('Percentage'))
            split.amount = _split.get('Percentage') * total_amount / 100
        splits.append(split)
    return generate_expense(title, expense_type, total_amount, paid_by, splits)
