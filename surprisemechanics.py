import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
playHandOne = random.randint(1,10)
playHandTwo = random.randint(1,10)
playHandTotal = playHandOne + playHandTwo
dealHandOne = random.randint(1,10)
dealHandTwo = random.randint(1,10)
dealHandTotal = dealHandOne + dealHandTwo
money = 100

def hitOrStay():
    playHandX = random.randint(1,10)
    hitOrStayvar = int(input("Would you like to \n 1. Hit \n 2. Stay "))
    while(hitOrStayvar == 1):
      playHandX = random.randint(1,10)
      playHandTotalX = playHandTotal + playHandX
      print("Your new card is ", playHandX,". Your total is now ",playHandTotalX)
      if(playHandTotalX >= 22):
        print("You went over 22 and bust! You automatically lost!")
        money == money - (bet)
      else:
        hitOrStayvar = int(input("Would you like to \n 1. Hit \n 2. Stay "))
    if(hitOrStayvar == 2):
      print("The dealer's second card is", dealHandTwo,". The dealer's total is ",dealHandTotal)
      if(dealHandTotal > playHandTotal or playHandTotalX):
        print("The dealer has a higher card. You lose!")
        money == money - (bet)
      elif(playHandTotal or playHandTotalX > dealHandTotal):
        print("You have a higher hand then the dealer. You win!")
        money == money + (bet)
      elif(dealHandTotal >= 22):
        print("The dealer went over 21 and hit bust! You win!")
        money == money + (bet)
      elif(dealHandTotal == playHandTotalX or playHandTotal):
        print("You had the same outcome! Draw!")
        money == money

def hitOrStaySplit():
  print("You have two hands now. Your first is ", handSplitOne, " and your second is ", handSplitTwo,".")
  hitStaySplit = int(input("Would you like to hit or stay on your first split? \n 1. Hit \n 2. Stay "))
  while(hitStaySplit == 1):
    playSplitX = random.randint(1,10)
    playSplitTotal = handSplitOne + playSplitX
    print("Your new card is ", playSplitX,". Your total is now ",playSplitTotal)
    if(playSplitTotal >= 22):
      print("You went over 22 and bust! You automatically lost!")
      money == money - (bet)
  if(hitStaySplit == 2):
    hitStaySplitTwo = int(input("Would you like to hit or stay on your second split? \n 1. Yes \n 2. No "))
    while(hitStaySplitTwo == 1):
      playSplitTwoX = random.randint(1,10)
      playSplitTwoTotal = handSplitTwo + playSplitTwoX
      print("Your new card is ", playSplitTwoX,". Your total is now ",playSplitTwoTotal)
      hitStaySplitTwo == int(input("Would you like to hit or stay on your second split? \n 1. Yes \n 2. No "))
      if(playSplitTwoTotal >= 22):
        print("You went over 22 and bust! You automatically lost!")
      else:
        hitStaySplit = int(input("Would you like to \n 1. Hit \n 2. Stay "))
    if(hitStaySplitTwo == 2):
      print("The dealer's second card is", dealHandTwo,". The dealer's total is ",dealHandTotal)
      while(dealHandTotal <= 16):
        dealHandX = random.randint(1,10)
        dealHandTotal == dealHandTotal + dealHandX
        print("The dealer is below 16 and must hit!")
        print("The dealer hit a ", dealHandX, ". Their total is now ", dealHandTotal)
      if(dealHandTotal > hitStaySplit and hitStaySplitTwo):
        print("The dealer has a higher number than both your splits. You lose!")
        money == money - (bet)
        playAgain()
      elif(hitStaySplit or hitStaySplitTwo > dealHandTotal):
        print("You have a higher hand then the dealer You win!")
        money == money + (bet)
        playAgain()
      elif(dealHandTotal >= 22):
        print("The dealer went over 21 and hit bust! You win!")
        money == money + (bet)
        playAgain()
      elif(dealHandTotal == hitStaySplit and hitStaySplitTwo):
        print("You had the same outcome! Draw!")
        money == money
        playAgain()

#Surprise mechanics
money = int(100)
while(money > 0):
  gameChoose = int(input("Do you want to play: \n 1. Blackjack \n 2. Dice \n use 1 for blackjack and 2 for dice. "))
# blackjack
  if(gameChoose == 1):
    print("You have ", money, " dollars left.")
    bet = int(input("How much would you like to bet? "))
    if(bet > money):
      bet = int(input("You don't have that much money. Input an amount you can bet: "))
    print("Your two cards are ", playHandOne, " and ", playHandTwo,". Your total is now ",playHandTotal)
    print("The dealer's first card is ",dealHandOne)
    if(playHandOne == 1 or playHandTwo == 1):
      aceMe = int(input("You have an Ace! Would you like to turn it into an 11? 1. Yes \t 2. No"))
      if(aceMe == 1):
        if(playHandOne == 1):
          playHandOne = 11
          print("Your new cards are ",playHandOne, " and ",playHandTwo)
          hitOrStay()
        elif(playHandTwo == 1):
          playHandTwo = 11
          print("Your new cards are ",playHandOne, " and ",playHandTwo)
          hitOrStay()
        elif(playHandOne == 1 and playHandTwo == 1):
          hitOrStaySplit()
    if(playHandOne == playHandTwo):
      splitMe = int(input("Your two cards are the same. You can split them into two different hands. Want to do that? \n 1. Yes \n 2. No"))
      if(splitMe == 1):
        handSplitOne = playHandOne
        handSplitTwo = playHandTwo
        hitOrStaySplit()
      elif(splitMe == 2):
        print("You have chosen not to split your cards.")
        hitOrStay()
    hitOrStay()
# dice
  if(gameChoose == 2):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("You have ", money, " dollars left.")
    bet = int(input("How much would you like to bet? "))
    if(bet > money):
      bet = int(input("You don't have that much money. Input an amount you can bet: "))
    if(dice1 == dice2):
      print("Dice 1 and Dice 2 are equal. You get your money back.")
      money = money
    elif(dice1 > dice2):
      print("Dice 1 is greater than Dice 2. You win double what you bet!")
      money = money + (bet)
    elif(dice2 > dice1):
      print("Dice 2 is greater than Dice 1. You lose what you bet!")
      money = money - (bet)
if(money <= 0):
  print("You lose all your money!")
  SystemExit

def playAgain():
  playMe = input("Would you like to play again? \n 1. Yes \n 2. No ")
  if(playMe == "1"):
    gameChoose = 1
  elif(playMe == "2"):
    SystemExit