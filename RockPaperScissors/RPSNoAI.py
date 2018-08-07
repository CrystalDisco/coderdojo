import random
compsignstr = 'Nothing.'
playersign = 'Nothing.'
win = 1
while True:
  computersign = random.randint(1,3)
  if computersign == 1:
    compsignstr = 'rock'
  elif computersign == 2:
    compsignstr = 'paper'
  elif computersign == 3:
    compsignstr = 'scissors'
  else:
    compsignstr = 'error'
  playersign = input('Rock, paper, or scissors? ')
  playersign = playersign.lower()
  print('Computer played', compsignstr + '.')
  print('You played', playersign +'.')
  if playersign == 'rock' and compsignstr == 'rock' or playersign == 'paper' and compsignstr == 'paper' or playersign == 'scissors' and compsignstr == 'scissors':
    print('It is a tie!')
    win = 1
  elif playersign == 'rock' and compsignstr == 'paper' or playersign == 'scissors' and compsignstr == 'rock' or playersign == 'paper' and compsignstr == 'scissors':
    print('Computer wins!')
    win = 0
  elif playersign == 'rock' and compsignstr == 'scissors' or playersign == 'scissors' and compsignstr == 'paper' or playersign == 'paper' and compsignstr == 'rock':
    print('Congratulations! You win!')
    win = 1
  else:
    print('An error has occured. Please check any spelling mistakes in your answer.')
  if win == 1:
    yn = input('Would you like to play again? (Y/N) ')
  else:
    yn = input('Would you like to try again? (Y/N) ')
  if yn.lower() == 'n':
    exit()
