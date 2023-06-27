n=18
play=1
print("you have only 5 chance to play\n")
while(play<=5):
  userInput=int(input("give number::"));
  if userInput<n:
    print("your guess is smaller",userInput)
    print("play again\n")
  elif userInput>n:
    print("your guess is bigger:",userInput)
    print("play again\n")
  else:
     print("you win \n")
     print("you play:",play,":time")
     break
print(5-play,":play you left")
if userInput>5:
  print("game over")