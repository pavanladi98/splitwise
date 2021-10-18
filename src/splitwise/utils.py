

def validate_email(email):
    if not isinstance(email, str):
        return False
    # todo: to be implemented
    return True


def validate_phone(phone):
    if not isinstance(phone, str):
        return False
    # todo: to be implemented
    return True


def validate_name(name):
    limit = 20 # todo: to be taken from config
    if not isinstance(name, str):
        return False
    if len(name) > limit:
        return False
    return True
