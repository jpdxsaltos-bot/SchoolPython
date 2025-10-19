attempts = 0
while attempts < 5:
    username = input("Enter username:")
    password = input("Enter password:")

    if username == "python" and password == "rules":
        print("Welcome!")
        break
    else:
        print("Incorrect username or password.")
        attempts += 1

if attempts == 5:
    print("Access denied.")