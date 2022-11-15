
MIN_LENGTH = 6
password = int(input("Enter password:"))
while MIN_LENGTH < len(password):
    print("Invalid")
    password = int(input("Enter password:"))
print("*" * len(password))
