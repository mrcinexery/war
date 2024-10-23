"""
Module represents the deck class.
"""
import random
from card import Card


class Deck:
    """
    Represents a deck of cards for the game War.

    The Deck class models a standard deck of 52 playing cards, consisting of four suits:
    spades, hearts, clubs, and diamonds. Each suit contains cards ranging from 2 to Ace.
    The class provides methods for initializing the deck, shuffling the cards, and splitting
    the deck into two halves for two players.

    Attributes:
        cards (list): A list that contains Card objects representing the deck.

    Methods:
        init_deck(): Initializes the deck with 52 cards, one for each combination of value and suit,
                     and shuffles them.
        get_first_half_deck(): Returns the first half of the deck as a new Deck object.
        get_second_half_deck(): Returns the second half of the deck as a new Deck object.
        get_cards(): Returns the list of cards in the deck.
        get_size(): Returns the number of cards remaining in the deck.
        get_top_card(): Returns the top card from the deck and removes it.
        set_cards(cards): Sets a list of cards as the deck.
    """

    def __init__(self):
        self.cards = []

    def __str__(self):
        for card in self.cards:
            return f'Card: {card}'

    def init_deck(self):
        """
        Function to initialise the deck with cards of a standard card deck.
        """
        card_deck = [
                ('Two of spades', 'spade', 2),
                ('Three of spades', 'spade', 3),
                ('Four of spades', 'spade', 4),
                ('Five of spades', 'spade', 5),
                ('Six of spades', 'spade', 6),
                ('Seven of spades', 'spade', 7),
                ('Eight of spades', 'spade', 8),
                ('Nine of spades', 'spade', 9),
                ('Ten of spades', 'spade', 10),
                ('Jack of spades', 'spade', 11),
                ('Queen of spades', 'spade', 12),
                ('King of spades', 'spade', 13),
                ('Ace of spades', 'spade', 14),
                ('Two of hearts', 'heart', 2),
                ('Three of hearts', 'heart', 3),
                ('Four of hearts', 'heart', 4),
                ('Five of hearts', 'heart', 5),
                ('Six of hearts', 'heart', 6),
                ('Seven of hearts', 'heart', 7),
                ('Eight of hearts', 'heart', 8),
                ('Nine of hearts', 'heart', 9),
                ('Ten of hearts', 'heart', 10),
                ('Jack of hearts', 'heart', 11),
                ('Queen of hearts', 'heart', 12),
                ('King of hearts', 'heart', 13),
                ('Ace of hearts', 'heart', 14),
                ('Two of clubs', 'clubs', 2),
                ('Three of clubs', 'clubs', 3),
                ('Four of clubs', 'clubs', 4),
                ('Five of clubs', 'clubs', 5),
                ('Six of clubs', 'clubs', 6),
                ('Seven of clubs', 'clubs', 7),
                ('Eight of clubs', 'clubs', 8),
                ('Nine of clubs', 'clubs', 9),
                ('Ten of clubs', 'clubs', 10),
                ('Jack of clubs', 'clubs', 11),
                ('Queen of clubs', 'clubs', 12),
                ('King of clubs', 'clubs', 13),
                ('Ace of clubs', 'clubs', 14),
                ('Two of diamonds', 'diamonds', 2),
                ('Three of diamonds', 'diamonds', 3),
                ('Four of diamonds', 'diamonds', 4),
                ('Five of diamonds', 'diamonds', 5),
                ('Six of diamonds', 'diamonds', 6),
                ('Seven of diamonds', 'diamond', 7),
                ('Eight of diamonds', 'diamond', 8),
                ('Nine of diamonds', 'diamond', 9),
                ('Ten of diamonds', 'diamond', 10),
                ('Jack of diamonds', 'diamond', 11),
                ('Queen of diamonds', 'diamond', 12),
                ('King of diamonds', 'diamond', 13),
                ('Ace of diamonds', 'diamond', 14)
        ]
        self.cards = []
        for card in card_deck:
            self.cards.append(Card(card[0], card[1], card[2]))
        random.shuffle(self.cards)

    def get_first_half_deck(self):
        """
        Function to return the first half of a deck
        :return: deck
        """
        half_deck = Deck()
        half_deck.cards = self.cards[:int(len(self.cards)/2)]
        random.shuffle(half_deck.cards)
        return half_deck

    def get_second_half_deck(self):
        """
        Function to return the second half of a deck
        :return: deck
        """
        half_deck = Deck()
        half_deck.cards = self.cards[int(len(self.cards) / 2):]
        random.shuffle(half_deck.cards)
        return half_deck

    def get_cards(self):
        """
        Function to return cards of the card deck.
        :return: cards
        """
        return self.cards

    def get_size(self):
        """
        Function to return the size of the card deck.
        :return: size of deck
        """
        return len(self.cards)

    def get_top_card(self):
        """
        Function to return the top card of the deck
        :return: a card
        """
        if len(self.cards) > 0:
            return self.cards.pop()
        return None

    def set_cards(self, cards):
        """
        Function to set cards within a deck
        :param cards: cards
        """
        self.cards = cards
