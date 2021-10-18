from .models import User, Expense
from .expense_repository import ExpenseRepository
from .exceptions import InvalidUserException, InvalidExpenseException


class ExpenseService:

    @staticmethod
    def create_expense(expense: Expense):
        if not expense.validate():
            raise InvalidExpenseException("Enter valid expense details")
        ExpenseRepository.add_expense(expense)

    @staticmethod
    def create_user(user: User):
        if not user.validate():
            raise InvalidUserException("Enter valid user details")
        ExpenseRepository.add_user(user)

    @staticmethod
    def get_user(user_id) -> User:
        return ExpenseRepository.get_user(user_id)

    @staticmethod
    def get_balance_sheet(user_id):
        user = ExpenseRepository.get_user(user_id)
        if not user:
            raise InvalidUserException("Enter valid user id")
        return ExpenseRepository.get_balance_sheet(user_id)

    @staticmethod
    def settle_balance(user_id_1, user_id_2):
        user1 = ExpenseRepository.get_user(user_id_1)
        if not user1:
            raise InvalidUserException("User {user_id_1} doesn't exist")
        user2 = ExpenseRepository.get_user(user_id_2)
        if not user2:
            raise InvalidUserException("User {user_id_2} doesn't exist")
        ExpenseRepository.settle_balance(user_id_1, user_id_2)
