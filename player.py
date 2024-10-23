"""
Module represents the player class.
"""
from deck import Deck


class Player:
    """
    Represents a player in the War game. This class contains attributes
    and methods related to managing the player's details, such as name,
    deck, and score.
    """

    def __init__(self, player='', name='', score=0):
        self.player = player
        self.name = name
        self.score = score
        self.deck = Deck()
        self.side_deck = Deck()

    def __str__(self):
        return (f'Player: {self.player}\n'
                f'Name: {self.name}\n'
                f'Deck size: {self.deck.get_size()}\n'
                f'Side deck size: {self.side_deck.get_size()}\n'
                f'Wins: {self.score}')

    def get_player(self):
        """
        Function to return player attr of a player.
        :return: Player attr of the player
        """
        return self.player

    def get_name(self):
        """
        Function to return name of a player.
        :return: Name of the player
        """
        return self.name

    def get_score(self):
        """
        Function to return score of a player.
        :return: Score of the player
        """
        return self.score

    def print_stats(self):
        """
        Function to print stats of a player.
        """
        print(f'Player:: {self.player}, Name: {self.name},'
              f'Score: {self.score}')

    def set_name(self, name):
        """
        Function to set the name of a player
        :param name: Name of the player
        """
        self.name = name

    def set_deck(self, deck):
        """
        Function to set the deck of a player
        :param deck: a deck of cards
        """
        self.deck = deck

    def increment_score(self):
        """
        Function to increment the score of the player.
        """
        self.score += 1

    def input_name(self):
        """
        Function to input name of player.
        """
        while self.name == '':
            self.set_name(input(f'What is your name {self.get_player()}? '))

    def get_deck(self):
        """
        Function to return the deck of the player.
        :return: a deck
        """
        return self.deck

    def get_side_deck(self):
        """
        Function to return the side deck of the player.
        :return: a deck
        """
        return self.side_deck

    def get_deck_size(self):
        """
        Function to return the size of the deck.
        :return: size
        """
        return self.deck.get_size()

    def get_side_deck_size(self):
        """
        Function to return the size of the side deck.
        :return: size
        """
        return self.side_deck.get_size()


    def put_on_side_deck(self, card):
        """
        Function to put a card on the side deck
        :param card: card of the deck
        """
        self.get_side_deck().get_cards().append(card)

    def put_under_deck(self, cards):
        """
        Function to put list of cards under the deck
        :param cards: cards
        [1, 2, 3, 4, 5] 1 last element 5 first element
        """
        self.get_deck().get_cards().reverse()

        if isinstance(cards, list):
            self.get_deck().get_cards().extend(cards)
        else:
            self.get_deck().get_cards().append(cards)

        self.get_deck().get_cards().reverse()







