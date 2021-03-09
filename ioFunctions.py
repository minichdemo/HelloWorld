def getIntegerInput(prompt):
  while True:
    try:
      userInput = int(input(prompt))       
    except ValueError:
      print("Not an integer! Try again.")
      continue
    else:
      return userInput 
      break 

def getBasicBoard(x):

  output = ""

  # display position labels
  for i in range(len(x)):
    #print(i + 1, end="")
    output += str(i + 1) + "\t"
    #print("\t", end="")
  
  #print()
  output += "\n"

  # values
  for i in range(len(x)):
    if x[i] == -1:
      #print("O", end="")
      output += "O"
    elif x[i] == 0:
      #print(" ", end="")
      output += " "
    else:
      #print("X", end="")
      output += "X"
    #print("\t", end="")
    output += "\t"

  return output
