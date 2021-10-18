from ..utils import validate_email, validate_phone, validate_name


class User:
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def validate(self):
        if not any([self.id, self.name, self.email, self.phone]):
            return False
        if not isinstance(self.id, int):
            return False
        return validate_email(self.email) and validate_phone(self.phone) and validate_name(self.name)

    # @property
    # def id(self):
    #     return self._id

    # @id.setter
    # def id(self, id):
    #     self._id = id

    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # def name(self, name):
    #     self._name = name

    # @property
    # def phone(self):
    #     return self._phone

    # @phone.setter
    # def phone(self, phone):
    #     self._phone = phone
