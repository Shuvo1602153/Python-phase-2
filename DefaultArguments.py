def greetings(name, message="Assala mualaikum"):
    return f"{message} , {name}"

message = input("Please Leave a Message: ")
name = input("What is your name ? : ")

if message:
    print(greetings(name, message))
else:
    print(greetings(name))