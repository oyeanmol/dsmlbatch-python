
def password_validation(password):
    if len(password) >= 8:
        lower = False
        upper = False
        digit = False
        special = False
        for i in password:
            if i.isupper():
                upper = True
            elif i.islower():
                lower = True
            elif i.isdigit():
                digit = True
            elif not i.isalnum():
                special = True
        if all([lower, upper, digit, special]):
            return True
        else:
            return False
    else:
        return False

