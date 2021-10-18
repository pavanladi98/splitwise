from .user import User


class Split:
    def __init__(self, user: User):
        self.user = user
        self.amount = 0

class EqualSplit(Split):
    def __init__(self, user: User):
        super(EqualSplit, self).__init__(user)

class ExactSplit(Split):
    def __init__(self, user: User, amount: float):
        super(ExactSplit, self).__init__(user)
        self.amount = amount

class PercentageSplit(Split):
    def __init__(self, user: User, percentage: float):
        super(PercentageSplit, self).__init__(user)
        self.percentage = percentage
