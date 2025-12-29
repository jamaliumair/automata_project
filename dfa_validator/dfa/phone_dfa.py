def check_phone(phone):
    if phone.startswith("+92") and len(phone) == 13:
        return phone[3:].isdigit()

    if phone.startswith("03") and len(phone) == 11:
        return phone.isdigit()

    return False
