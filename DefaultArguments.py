def hello_function(name, message ='Hello'):
    return f"{message} ,{name}"
message = input('please left a message')
name = input ("What is your name :")

print(hello_function(name,message))
