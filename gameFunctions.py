def isThereAWin(gameState):
  # checks for a winner
  
  return isThereAWinInAnyRow(gameState) or isThereAWinInAnyColumn(gameState)


def isThereAWinInAnyRow(gameState):
  # checks for a winner in any row
  
  # checking for x wins

  # top row
  if gameState[0] == 1 and gameState[1] == 1 and gameState[2] == 1:
    print("DEBUGGING: top row 1")
    return True

  # middle row
  if gameState[3] == 1 and gameState[4] == 1 and gameState[5] == 1:
    print("DEBUGGING: middle row 1")
    return True

  # bottom row
  if gameState[6] == 1 and gameState[7] == 1 and gameState[8] == 1:
    print("DEBUGGING: bottom row 1")
    return True
  
  # checking for o wins

  # top row
  if gameState[0] == -1 and gameState[1] == -1 and gameState[2] == -1:
    print("DEBUGGING: top row -1")
    return True

  # middle row
  if gameState[3] == -1 and gameState[4] == -1 and gameState[5] == -1:
    print("DEBUGGING: middle row -1")
    return True

  if gameState[6] == -1 and gameState[7] == -1 and gameState[8] == -1:
    print("DEBUGGING: bottom row -1")
    return True

  # no winner in any row
  return False


def isThereAWinInAnyColumn(gameState):
  # checks for a winner in any column
  
  # checking for x wins

  # left column
  if gameState[0] == 1 and gameState[3] == 1 and gameState[6] == 1:
    print("DEBUGGING: left column 1")
    return True

  # no winner in any column
  return False

