while True:
    password = input("Enter password: ")

    if password == "stop":
        break

    upper = False
    lower = False
    digit = False

    for ch in password:
        if ch.isupper():
            upper = True
        if ch.islower():
            lower = True
        if ch.isdigit():
            digit = True

    if len(password) >= 8 and upper and lower and digit:
        print("Strong password")
    else:
        print("Weak password")