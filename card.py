"""
Module represents the card class.
"""

class Card:
    """
    Represents a card for the game War.
    """
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'{self.name}'

    def get_card(self):
        """
        Function to return card obj
        :return: card
        """
        return {'name': self.name, 'suit': self.suit, 'value': self.value}

    def get_value(self):
        """
        Function to return the value of a card
        :return: value
        """
        return self.value

    def get_suit(self):
        """
        Function to return the suit of a card
        :return: str
        """
        return self.suit


    def get_name(self):
        """
        Function to return the name of a card
        :return: name
        """
        return self.name

    def set_card(self, name, suit, value):
        """
        Function to set name, suit and value of a card
        :param name: name of the card
        :param suit: suit of the card
        :param value: value of the card
        """
        self.name = name
        self.suit = suit
        self.value = value
