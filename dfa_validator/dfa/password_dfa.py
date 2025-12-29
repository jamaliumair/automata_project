def check_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_symbol = True

    if has_upper and has_lower and has_digit and has_symbol:
        return True
    return False
