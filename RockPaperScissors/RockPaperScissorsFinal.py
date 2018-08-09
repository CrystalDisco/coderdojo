# Import statements, currently just random for generation later in the script.
import random

# Variable initialisation.
compsignstr = 'Nothing.'
playersign = 'Nothing.'
prevsign1 = 'Nothing.'
prevsign2 = 'Nothing.'
prevsign3 = 'Nothing.'
# These variables will be used for the scoreboard
playerwins = 0
computerwins = 0
# A syntax variable, determining whether you would like to 'try' again or 'play' again.
win = 1

# Asks if the user would like to turn on single mode, which allows the entry of a single character rather than the full string. 
singlemode = input('Would you like to turn on single character mode? (This allows you to use "R", "P", and "S" instead of the full string.)(Type RPS to enable.) ')
if singlemode.upper() == 'RPS':
  singlemode = True
  print('\nSingle Character mode enabled.\n')
else:
  print('\nSingle Character mode not enabled.\n')
# While True is used as an infinite loop, allowing the script to be run multiple times rather than reopening the script constantly
while True:
  # Now it gets complicated. The 'prevsign' variables are used for determining what your next move will be. If prevsign3 wasn't filled out, it will continue random number generation until it was. This can be achieved by typing in a wrong answer and pushing it through to prevsign3 if you wanted to.
  if prevsign3 == 'Nothing.':
    computersign = random.randint(1,3)
  # Determining answer from previous responses if applicable. Otherwise, just leaving it to RNG.
  else:
      if prevsign1 == prevsign2:
        if prevsign1 == 3:
          computersign = 1
        elif prevsign1 == 1 or prevsign1 == 2:
          computersign = prevsign1 + 1
        else:
          computersign = random.randint(1,3)
      else:
        computersign = random.randint(1,3)
  # Converting numeric answer into a legible string for later operations and legible displayability.
  if computersign == 1:
    compsignstr = 'rock'
  elif computersign == 2:
    compsignstr = 'paper'
  elif computersign == 3:
    compsignstr = 'scissors'
  else:
    compsignstr = 'error'
  # Grabs input from the player, turns it lowercase, and determines the winner based on the string. If single mode was turned on, also transforms input into the full string.
  playersign = input('Rock, paper, or scissors? ')
  playersign = playersign.lower()
  if singlemode == True:
    if playersign == 'r':
      playersign = 'rock'
    elif playersign == 'p':
      playersign = 'paper'
    elif playersign == 's':
      playersign = 'scissors'
    else:
      playersign = playersign
  print('Computer played', compsignstr + '.')
  print('You played', playersign +'.')

  if playersign == 'rock' and compsignstr == 'rock' or playersign == 'paper' and compsignstr == 'paper' or playersign == 'scissors' and compsignstr == 'scissors':
    print('It is a tie!')
    win = 1
  elif playersign == 'rock' and compsignstr == 'paper' or playersign == 'scissors' and compsignstr == 'rock' or playersign == 'paper' and compsignstr == 'scissors':
    print('Computer wins!')
    computerwins = computerwins + 1
    win = 0
  elif playersign == 'rock' and compsignstr == 'scissors' or playersign == 'scissors' and compsignstr == 'paper' or playersign == 'paper' and compsignstr == 'rock':
    print('Congratulations! You win!')
    playerwins = playerwins + 1
    win = 1
  else:
    print('An error has occured. Please check any spelling mistakes in your answer.')
  # Prints out the scoreboard.
  print('\nThe current scores are:')
  print('You:', playerwins)
  print('Computer:', computerwins)
  # Asks if the player would like to play again (see above 'win' variable explanation). If not, breaks out of the loop and thanks you for playing. Otherwise, no break occurs and it restarts.
  if win == 1:
    yn = input('Would you like to play again? (Y/N) ')
  else:
    yn = input('Would you like to try again? (Y/N) ')
  if yn.lower() == 'n':
    break
  prevsign3 = prevsign2
  prevsign2 = prevsign1
  if yn.lower() == 'y':
    if playersign == 'rock':
      prevsign1 = 1
    elif playersign == 'paper':
      prevsign1 = 2
    elif playersign == 'scissors':
      prevsign1 = 3
    else:
      prevsign1 = 'Nothing.'
print('\nThank you for playing!')
exit()
