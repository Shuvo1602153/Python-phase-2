def greetings(name,message="Hello"):
    return f"{message},{name}"



message =input("Please left a message :")

name =input("what is your name :")

if message:
    print(greetings(name,message))
else:
    print( greetings(name))