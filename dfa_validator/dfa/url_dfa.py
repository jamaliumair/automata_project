def check_url(url):
    state = 0
    i = 0

    while i < len(url):
        ch = url[i]

        if state == 0 and url.startswith("http://", i):
            state = 1
            i += 7
            continue
        elif state == 0 and url.startswith("https://", i):
            state = 1
            i += 8
            continue

        elif state == 1 and ch.isalnum():
            state = 2

        elif state == 2 and ch.isalnum():
            pass
        elif state == 2 and ch == '.':
            state = 3

        elif state == 3 and ch.isalpha():
            state = 4

        elif state == 4 and ch.isalpha():
            pass
        elif state == 4 and ch == '/':
            state = 5

        elif state == 5:
            pass
        else:
            return False

        i += 1

    return state in [4, 5]
