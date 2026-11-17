def configure_ai_tool(model= "gpt-4",temperature= 0.7, max_tokens= 500,mode="Standard"):
    return f"Model = {model}\nTemperature = {temperature}\nMaximum tokens = {max_tokens}\nMode = {mode}"

model = input("Please write your desire model name: ")
temperature= input("Please input a temperature: ")
max_tokens = input("Please select a Maximum tokens: ")
mode = input("Please insert a Mode: ")

if model and temperature and max_tokens and mode:
  print(configure_ai_tool(model=model, temperature=float(temperature),max_tokens=int(max_tokens), mode=mode,))

elif model and temperature and max_tokens:
  print(configure_ai_tool( model=model,temperature=float(temperature), max_tokens=int(max_tokens),))

elif model and temperature and mode:
  print( configure_ai_tool(model=model, temperature=float(temperature), mode=mode))

elif model and max_tokens and mode:
  print(
      configure_ai_tool(model=model, max_tokens=int(max_tokens), mode=mode ))
  
elif temperature and max_tokens and mode:
  print(configure_ai_tool(temperature=float(temperature),max_tokens=int(max_tokens),mode=mode,) )

elif model and temperature:
  print(configure_ai_tool(model=model, temperature=float(temperature)))

elif model and max_tokens:
  print(configure_ai_tool(model=model, max_tokens=int(max_tokens)))

elif model and mode:
  print(configure_ai_tool(model=model, mode=mode))

elif temperature and max_tokens:
  print(configure_ai_tool( temperature=float(temperature), max_tokens=int(max_tokens) ))

elif temperature and mode:
  print( configure_ai_tool(temperature=float(temperature), mode=mode))

elif max_tokens and mode:
  print(configure_ai_tool(max_tokens=int(max_tokens), mode=mode) )

elif model:
  print(configure_ai_tool(model=model))

elif temperature:
  print(configure_ai_tool(temperature=float(temperature)))

elif max_tokens:
  print(configure_ai_tool(max_tokens=int(max_tokens)))
  
elif mode:
  print(configure_ai_tool(mode=mode))