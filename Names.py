names = set()

while True:
    name = input("Enter a name (or press Enter to quit):")
    if name == "":
        break
    if name not in names:
        print("New name")
        names.add(name)
    else:
        print("Existing name")

print("All names entered:")
for name in names:
    print(name)