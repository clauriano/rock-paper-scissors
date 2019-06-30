import random
possible = ["rock", "paper", "scissors"]
score = 0
computerScore = 0

while score < 11 and computerScore < 10:
  integer = random.randint(0,2)
  computer = possible[integer]
  humanPlayer = input("Pick rock, paper, or scissors: ")

  if humanPlayer not in possible:
    print("Invalid entry")
  elif humanPlayer == computer:
    print("You tied.")

  elif humanPlayer != computer:
    if humanPlayer == "rock" and computer == "scissors":
      score += 1
      print("You win. Computer chose " + computer + ". Your score: " + str(score))
    elif humanPlayer == "paper" and computer == "rock":
      score += 1
      print("You win. Computer chose " + computer + ". Your score: " + str(score))
    elif humanPlayer == "scissors" and computer == "paper":
      score += 1
      print("You win. Computer chose " + computer + ". Your score: " + str(score))
    else:
      computerScore += 1
      print("Computer choose " + computer + ". Computer wins. Computer's score: " + str(computerScore))