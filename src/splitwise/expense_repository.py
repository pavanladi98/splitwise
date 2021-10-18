from .models import User, Expense
from .exceptions import UserAlreadyExistsException


class ExpenseRepository:
    expenses = list()
    users = dict()
    balance_sheet = dict()

    def add_user(user: User) -> None:
        if ExpenseRepository.users.get(user.id):
            raise UserAlreadyExistsException(
                f'User already exists with id:{user.id}')
        ExpenseRepository.users[user.id] = user
        ExpenseRepository.balance_sheet[user.id] = {}

    def get_user(user_id: str) -> User:
        if not ExpenseRepository.users.get(user_id):
            return
        return ExpenseRepository.users[user_id]

    def add_expense(expense: Expense) -> None:
        ExpenseRepository.expenses.append(expense)
        for split in expense.splits:
            paid_to = split.user.id
            balances = ExpenseRepository.balance_sheet[expense.paid_by.id]
            if not balances.get(paid_to):
                balances[paid_to] = 0
            balances[paid_to] += split.amount

            balances = ExpenseRepository.balance_sheet[paid_to]
            if not balances.get(expense.paid_by.id):
                balances[expense.paid_by.id] = 0
            balances[expense.paid_by.id] -= split.amount

    def settle_balance(user_id_1, user_id_2):
        balances = ExpenseRepository.balance_sheet[user_id_1]
        del balances[user_id_2]
        balances = ExpenseRepository.balance_sheet[user_id_2]
        del balances[user_id_1]

    def get_balance_sheet(user_id):
        formatted_balance_sheet = []
        for _user, _balance in ExpenseRepository.balance_sheet[user_id].items():
            if _balance != 0:
                formatted_balance = ExpenseRepository.get_formatted_balance(
                    user_id, _user, _balance)
                formatted_balance_sheet.append(formatted_balance)
        return formatted_balance_sheet

    def get_formatted_balance(user1, user2, amount):
        user1_name = ExpenseRepository.users[user1].name
        user2_name = ExpenseRepository.users[user2].name
        if amount < 0:
            return f"{user1_name} owes {user2_name} {abs(amount)}"
        elif amount > 0:
            return f"{user2_name} owes {user1_name} {abs(amount)}"
