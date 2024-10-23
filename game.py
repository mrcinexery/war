"""
Module represents the game class and contains the logic of the game.
"""


class Game:
    """
    Represents the logic of the card game War.

    The Game class controls the flow and rules of the card game War, played
    between two players. It manages the distribution of cards, checks for
    cyclic states to prevent infinite loops, and handles side decks in case of
    tied rounds. The game continues until one player has all the cards,
    or players choose to end the game.

    Attributes:
        player1 (Player): The first player in the game.
        player2 (Player): The second player in the game.
        previous_rounds (set): A set that stores the deck states of previous
        rounds to detect cyclic patterns in card distribution.
    """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.previous_rounds = set()

    def print_battle(self, card1, card2):
        """
        Function to print which cards battle with each other.
        :param card1: card of player1
        :param card2: card of player2
        :return:
        """
        if card1 is not None and card2 is not None:
            print(f'{card1.get_name()} ({self.player1.get_name()})'
                  f' fights against '
                  f'{card2.get_name()} ({self.player2.get_name()})')

    @staticmethod
    def print_rules():
        """
        Function to initialise the rules of the game.
        """
        print()
        print('###### Welcome to War! \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t'
              '######')
        print(
            '###### War is a simple card game played between two '
            'players. \t\t\t\t\t\t\t######')
        print(
            '###### Each player receives half of a shuffled deck of 52 '
            'cards. \t\t\t\t\t\t######')
        print(
            '###### In each round, both players draw the top card from their '
            'deck. \t\t\t\t\t######')
        print(
            '###### The player with the higher card wins the round and takes'
            'both cards.\t\t\t\t######')
        print('###### If the cards are of equal rank, both players put their '
              'card on a side stack. \t######')
        print('###### The winner of the next round takes both cards plus all'
              ' cards on the side stacks. ######')
        print(
            '###### The game continues until one player has all the'
            ' cards \t\t\t\t\t\t\t######')
        print(
            '###### Thus the goal is to capture all of your opponent’s cards.'
            ' \t\t\t\t\t\t######')
        print('')
        print(
            'Let\'s start by choosing the names of the players...')

    def save_deck_state(self):
        """
        Function to save the current state of the decks as a hash (tupel)
        and add this to the set 'previous_rounds'.
        """
        deck1_state = tuple((card.get_value(), card.get_suit())
                            for card in self.player1.get_deck().get_cards())
        deck2_state = tuple((card.get_value(), card.get_suit())
                            for card in self.player2.get_deck().get_cards())
        return deck1_state, deck2_state

    def is_cyclic(self):
        """
        Function to check if the current state of the decks appeared in past.
        If True, there is cyclic distribution discovered and the game ends.
        """
        current_state = self.save_deck_state()
        if current_state in self.previous_rounds:
            return True
        self.previous_rounds.add(current_state)
        return False

    def get_distributed_side_decks(self):
        """
        Function to return side decks of both player in alternate order
        :return: list
        """
        side_deck_cards = []

        while (self.player1.get_side_deck_size() > 0
               or self.player2.get_side_deck_size() > 0):
            if self.player1.get_side_deck_size() > 0:
                side_deck_cards.append(
                    self.player1.get_side_deck().get_cards().pop(-1))
            if self.player2.get_side_deck_size() > 0:
                side_deck_cards.append(
                    self.player2.get_side_deck().get_cards().pop(-1))

        return side_deck_cards

    @staticmethod
    def new_game():
        """
        Function to decide if players want to play a new game
        :return: True if players want to play a new game, False if they want
        not play a new game.
        """
        answer = ''
        while answer not in ['y', 'n']:
            answer = input('Would you play another game? (y/n)')
        if answer == 'y':
            return True
        return False
