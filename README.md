Class Game simulates simple card game. 

Game begins with deck of cards from [1,2,3 to deck size]. Cards are positive integers and they are all unique.

Games starts with shuffling the deck and dealing the cards to the players.

If during last deal there is not enough cards for all players, then random players receive remaining cards. 

During the round each player plays card from the top of their deck. Player with the biggest card takes all the cards played in the round and gets as many points as many card the player took. If during last round not all players have the cards left, then play the players with the cards only.

After players has no more cards to play the game is over. 

The game is won by the player with the highest amount of points. If there's a draw, players with the highest scores check their deck and the player who has higher card in the deck wins.

Class Game expects list of players names as the first parameter and the integer with the deck size as the second parameter. Method "who_won" simlates the game and returns information about the winner.