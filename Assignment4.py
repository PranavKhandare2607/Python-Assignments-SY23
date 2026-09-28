secret = input("Enter secret message: ")
message = input("Enter coded message: ")

if secret in message:
    print("Secret message found")
else:
    print("Secret message not found")