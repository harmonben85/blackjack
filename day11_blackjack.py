# Blackjack Project

from art import logo
import random
from replit import clear

# Deal Cards Function
def deal_cards(hand):
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
  
# Calculate Score Function
def calculate_score(hand):
  '''This function '''
  score = sum(hand)
  if score == 21 and len(hand) == 2:
    return 0
  if hand[0] == 11 or hand[1] == 11 and score > 21:
    hand.remove(11)
    hand.append(1)
    score = sum(hand)
    return score
  else:
    return score

def compare(users_score, dealers_score):
  if users_score > 21 and dealers_score > 21:
    return "You went over. You lose 😤"

  if users_score == dealers_score:
    return "\nDraw"
  elif dealers_score == 0:
    return "\nLose, opponent has Blackjack"
  elif users_score == 0:
    return "\nWin with a Blackjack"
  elif users_score > 21:
    return "\nYou went over. You lose"
  elif dealers_score > 21:
    return "\nOpponent went over. You win"
  elif users_score > dealers_score:
    return "\nYou win"
  else:
    return "\nYou lose"

def play():

  print(logo)
      
# Dealing Cards
  users_hand = []
  users_hand.append(deal_cards(users_hand))
  users_hand.append(deal_cards(users_hand))

  dealers_hand = []
  dealers_hand.append(deal_cards(dealers_hand))
  dealers_hand.append(deal_cards(dealers_hand))

  # Calculating Scores
  users_score = calculate_score(users_hand)
  dealers_score = calculate_score(dealers_hand)
  
  print(f"\nYour hand: {users_hand}\nYour score: {users_score}")
  print(f"\nThe dealers first card is {dealers_hand[0]}.")
  
  game_over = False
  while game_over == False:
  
    if users_score == 0 or dealers_score == 0 or users_score > 21:
      game_over = True
    else:
      users_choice = input("\nDo you want to hit or stand?: ").lower()
      
      if users_choice == "hit":
        users_hand.append(deal_cards(users_hand))
        users_score = sum(users_hand)
      else: 
        game_over = True
  
    while dealers_score != 0 and dealers_score < 17:
      dealers_hand.append(deal_cards(dealers_hand))
      dealers_score = sum(dealers_hand)

  print(f"\nYour final hand: {users_hand}, final score: {users_score}")
  print(f"\nDealer's final hand: {dealers_hand}, final score: {dealers_score}")
  print(compare(users_score, dealers_score))

while input("\nDo you want to play a game of Blackjack? Type 'yes' or 'no': ") == "yes":
  clear()
  play()


  