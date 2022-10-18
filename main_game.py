import random
import time
import sys
from art import logo
def s_player_cards():
  """Sum of player's cards"""
  sum_p_cards = 0
  return sum(p_cards)
def s_dealer_cards():
  """Sum of dealer's cards"""
  sum_d_cards = 0
  return sum(d_cards)
def check_final_score(s_p_cards, s_d_cards):
  """Checking the score, needs update"""
  if s_dealer_cards() > s_player_cards():
    return "You lost"
  elif s_player_cards() > s_dealer_cards():
    return "You win"
  else:
    return "It's a tie! You're lucky this time"
def check_player_score(s_player_cards):
  if s_player_cards() > 21:
    return "You went over 21. You lost!"
  else:
    return s_player_cards()
def ace(s_player,p_cards): 
  """Function to verify when an ace is 11 or 1"""
  if s_player_cards() > 21:
    for i in range(0,len(p_cards)):
      if p_cards[i] == 11:
        if s_player_cards() - 10 > 21:
          return "You lost!"
      else:
        return 0
def dealer_cards():
  while sum(d_cards) < 17:
    d_cards.append(random.choice(cards))
  if sum(d_cards) > 17:
    return d_cards
def blackjack(sum_dealer,sum_player):
  if sum_player == 21:
    return "It's a blackjack. You win"
  elif sum_dealer == 21:
    return "I'm sorry. Blackjack to dealer. You lose!"
  else:
    return 0
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
print(logo)
wanna_play = input("Do you want to play a blackjack game? Type 'y' or 'n' ").strip()
wanna_play = wanna_play.lower()
p_cards = random.sample(cards,2)
d_cards = random.sample(cards,2)
print(f"Your cards are {p_cards} , total = {s_player_cards()}")
print(f"Computer's first card is {d_cards[0]} \n")
if blackjack(s_dealer_cards(),s_player_cards()) != 0:
  print(blackjack(s_dealer_cards,s_player_cards))
  sys.exit()
get_card = input("Do you want to get another card? Type 'y' or 'n' ").strip()
while True:
  if get_card == 'n':
    break
  if get_card == 'y':
    p_cards.append(random.choice(cards))
    if blackjack(s_dealer_cards,s_player_cards) != 0:
      blackjack(s_dealer_cards,s_player_cards)
      break
    if ace(s_player_cards,p_cards) == "You lost!":
      ace(s_player_cards,p_cards)
    print(f"Your cards are {p_cards} , total = {s_player_cards()} \n")
    ace(s_player_cards,p_cards)
    if check_player_score(s_player_cards) != s_player_cards():
      dealer_cards()
      print(f"Computer's final cards are {d_cards} , total is {s_dealer_cards()}.")
    if check_player_score(s_player_cards) != s_player_cards():
      print(check_player_score(s_player_cards)) 
      break
    if s_player_cards() < 21:
      get_card = input("\nDo you want to get another card? Type 'y' or 'n' ").strip()
    else:
      break
if get_card == 'n':
  dealer_cards()
  s_dealer_cards()
  if s_dealer_cards() > 21:
    print(f"Your final cards are {p_cards} , total is {s_player_cards()}")
    print(f"Computer's final cards are {d_cards} , total is {s_dealer_cards()}.\n")
    print("You win!")
  else:
    print(f"Your final cards are {p_cards} , total is {s_player_cards()}")
    print(f"Computer's final cards are {d_cards} , total is {s_dealer_cards()}.\n")
    time.sleep(1)
    print(check_final_score(s_player_cards,s_dealer_cards))
    





    
      
  
  








