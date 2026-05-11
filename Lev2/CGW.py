import random
import time



cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K', 'A']             # '10 written as 'X'
suits = ['C', 'D', 'H', 'S']     # ‘C’ for ‘Clubs’; ‘D’ for ‘Diamonds’; ‘H’ for ‘Hearts’; ‘S’ for ‘Spades’

# Create a deck of cards (Another list that has all the combinations)

deck_of_cards = []; 

for kk in range(len(suits)):
    for jj in range(len(cards)):
        deck_of_cards.append(suits[kk]+cards[jj])


print('Unshuffled Deck:')
for kk in range(len(deck_of_cards)):
    print(deck_of_cards[kk], end = ' ')
print()
    
random.shuffle(deck_of_cards) 

print('Shuffled Deck:')
for kk in range(len(deck_of_cards)):
    print(deck_of_cards[kk], end = ' ')

# Toss 
# Pick one random card from the pile

toss = random.choice(deck_of_cards)
print()
if toss[0] == 'C' or toss[0] == 'D':
    first_mover = 'player'
    print('You won the toss, you will play first.')
else:
    first_mover = 'computer'
    print('Computer won the toss, it will play first')

# Deal the cards

player_cards = deck_of_cards[0:26:1]
comput_cards = deck_of_cards[26:52:1]
table_cards = []
# Both computer and the player pick up their first card. 

move_complete = False
game_complete = False
moves_played = 0

while not(game_complete):
  
  move_complete = False
  
  if len(player_cards)<1 or len(comput_cards)<1:
    move_complete = True
    game_complete = True
  
  while not(move_complete):
    card_p = player_cards.pop(0)
    card_c = comput_cards.pop(0)
    print()
    print('Player Card is ...', card_p)
    print('Computer Card is ...', card_c)
    

    table_cards.append(card_p)
    table_cards.append(card_c)
    
    if cards.index(card_p[1])>cards.index(card_c[1]):
      print('Player Wins ... ')
      input()
      player_cards.extend(table_cards)
      table_cards.clear()
      move_complete = True
      moves_played = moves_played + 1
    elif cards.index(card_p[1])<cards.index(card_c[1]):
      print('Computer Wins ... ')
      input()
      comput_cards.extend(table_cards)
      table_cards.clear()
      move_complete = True
      moves_played = moves_played + 1
    else:
			# WAR Begins. 
      print("War begins")
      input()
			# Check whether sufficient number of cards
      if len(player_cards)<4 or len(comput_cards)<4:
        move_complete = True
            	#game_complete = True
      else:
            	# Append these cards to the Table Cards.
        table_cards.extend(player_cards[0:3])
        table_cards.extend(comput_cards[0:3])

            	# Remove these cards from the player and computer cards.            
        del player_cards[0:3]
        del comput_cards[0:3]
    if moves_played == 100:
      game_complete = True
		
    print("Player Cards:", len(player_cards), "Computer Cards:", len(comput_cards), "Table Cards:", len(table_cards))    


print()
print()

# Game is over. Determine the winner. 
if len(player_cards) > len(comput_cards):
	print('PLAYER is the winner')
elif len(player_cards) < len(comput_cards):
	print('COMPUTER is the winner')
else:
	print('GAME drawn!')