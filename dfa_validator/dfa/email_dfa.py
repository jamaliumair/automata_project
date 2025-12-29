def check_email(email):
    state = 0

    for ch in email:
        if state == 0:
            if ch.isalnum():
                state = 1
            else:
                return False

        elif state == 1:
            if ch.isalnum():
                pass
            elif ch == '@':
                state = 2
            else:
                return False

        elif state == 2:
            if ch.isalnum():
                state = 3
            else:
                return False

        elif state == 3:
            if ch.isalnum():
                pass
            elif ch == '.':
                state = 4
            else:
                return False

        elif state == 4:
            if ch.isalpha():
                state = 5
            else:
                return False

        elif state == 5:
            if ch.isalpha():
                pass
            else:
                return False

    return state == 5
