#function
def token_cost(x):
    return x * 10

#dictionary
aiModel_costEstimetor={
"model" : "gpt-4",
"temperature" : 0.7,
"tokens" : 500,
"mode" : "standard"
}
token =500
#input
model = input ("please type a model (gpt-4 or gpt-3.5): ")

tokens = input("(per 1000 token =10 BDT) : ")
#type cast

if tokens:
    token=int(tokens)
else:
     tokens=tokens

mode = input ("type a mode ( standard or creative): ")
#validation

if model:
    aiModel_costEstimetor["model"]= model
if token:
    aiModel_costEstimetor["tokens"]=token_cost(token)
if mode:
    aiModel_costEstimetor["mode"]= mode
#output
print("configuration model =",aiModel_costEstimetor)