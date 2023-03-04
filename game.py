
import random

class Game:
    def __init__(self,list_of_user_names,deck_size):
        self.list_of_user_names = list_of_user_names
        self.deck_size = deck_size
        
    
    def __deal_cards__(self):
        amount_of_players = len(self.players_list)
        base_deck_size = self.deck_size // amount_of_players * amount_of_players
        cards_for_last_deck = self.deck_size % amount_of_players

        deck_for_game = []
        for i in range(1, self.deck_size + 1):
            deck_for_game.append(i)

        random.shuffle(deck_for_game)

        base_deck = deck_for_game[0:base_deck_size]
        extra_deck = deck_for_game[base_deck_size:]

        if (len (extra_deck) > 0):
            for i in range (amount_of_players - cards_for_last_deck):
                extra_deck.append(0)
                # print (i)

        random.shuffle(extra_deck)
        deck = base_deck + extra_deck

        for i in range (len(deck)):
            self.players_list[i%amount_of_players].start_deck.append(deck[i])


    def __play_game__ (self):

        #clear has_top_card variable - just in case
        for player in self.players_list:
            player.has_top_card = False

        # simulate game
        for i in range (len(self.players_list[0].start_deck)):
            scoring_player = 0
            scoring_card = 0
            points_for_deal = 0
            current_deal =[]
            current_player_no = 0 

            for player in self.players_list:
                current_deal.append (player.start_deck[i])
                if(player.start_deck[i])>0:
                    points_for_deal = points_for_deal + 1

                if (player.start_deck[i] > scoring_card):
                    scoring_player = current_player_no
                    scoring_card = player.start_deck[i]

                current_player_no += 1

            self.players_list[scoring_player].score += points_for_deal 
            self.players_list[scoring_player].end_deck += current_deal
            # print(current_deal)
            # print("Scoring player: {}, {} points.".format(scoring_player, points_for_deal))
    
    def who_won(self):

        # check if parameters provided by user are as expected
        if not isinstance (self.list_of_user_names,list):
            return ("ERROR: First parameter has to be list of user names")
        elif len(self.list_of_user_names) == 0:
            return ("ERROR: List of user names cannot be empty")
        elif not isinstance (self.deck_size,int):
            return ("ERROR: Deck size parameter has to be integer.")
        elif self.deck_size <= 0:
            return ("ERROR: Deck size parameter has to be bigger than 0.")

        # create list of players
        self.players_list = []
        for player_name in self.list_of_user_names:
            new_player = Player(player_name)
            # print(player_name)
            self.players_list.append(new_player)

        # let the game begin ;-)
        self.__deal_cards__()
        self.__play_game__()

        # identify the winner and return winning information
        winning_score = 0
        winning_players_pos = []
        
        # identify players with max. scores
        for player_no in range(len(self.players_list)):
            player = self.players_list[player_no]
            if player.score > winning_score:
                winning_players_pos.clear()
                winning_players_pos.append(player_no)
                winning_score = player.score
            elif player.score == winning_score:
                winning_players_pos.append (player_no)

        if len(winning_players_pos) > 1:
            # we have draw so the max card wins
            winning_player_no = 0
            max_card = 0
            for player_no in winning_players_pos:
                player = self.players_list[player_no]
                max_player_card = max(player.end_deck)
                if max_player_card > max_card:
                    winning_player_no = player_no
                    max_card = max_player_card
            winning_player = self.players_list[winning_player_no]
            return ("The winner is {} with {} points and card {}.".format(winning_player.name, winning_player.score,max_card))
            
        else:
            # we have clear winner
            winning_player = self.players_list[winning_players_pos[0]]
            return ("The winner is {} with {} points.".format(winning_player.name, winning_player.score))


class Player:
    def __init__(self,player_name):
        self.name = player_name
        self.start_deck = []
        self.end_deck = []
        self.score = 0
        # self.has_top_card = False


new_game = Game(["Mark","John","Lisa"],25)
print (new_game.who_won())

new_game2 = Game(["Mark","John","Lisa"],33333)
print (new_game2.who_won())
