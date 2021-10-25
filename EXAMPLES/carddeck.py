#!/usr/bin/env python
"""
Provide a CardDeck object and some utility methods
"""
import random

class CardDeck:
    """
    A deck of 52 cards for playing standard card games
    """
    # def __new__(): pass
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    DEALER_NAMES = []

    def __init__(self, dealer):
        """
        CardDeck constructor

        :param dealer: Name of dealer as a string
        """
        self.dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    def draw(self):
        """
        Retrieve next available card from deck.

        Raises IndexError when deck is empty.

        :return: One cards as a (rank, suit) tuple.
        """
        try:
            return self._cards.pop(0) #
        except IndexError:
            print("Sorry, no more cards")

    def shuffle(self):
        """
        Randomize the deck of cards

        :return: None
        """
        random.shuffle(self._cards)

    @property
    def dealer(self):  # getter property
        """
        Set/Retrieve the dealer.

        If invalid type is assigned, raises TypeError

        :return: Dealer as a string
        """
        return self._dealer

    @dealer.setter
    def dealer(self, value):  # setter property
        if isinstance(value, str):
            self._dealer = value
        else:
            raise TypeError("Dealer must be a string")

    @property
    def cards(self):
        """
        Retrieve cards

        :return:  a comma-separated string of cards
        """
        return ", ".join([f"{rank}-{suit[0]}" for rank, suit in self._cards])

    @classmethod
    def get_ranks(cls):
        """
        Return ranks as a list

        :return:
        """
        return cls.RANKS

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}({self.dealer},{len(self)})"

    def __repr__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"""{my_name}("{self.dealer}")"""

    def __add__(self, other):
        my_type = type(self)
        tmp = my_type(self.dealer)
        tmp._cards = self._cards + other._cards
        return tmp

    def __eq__(self, other):
        return (
            self.dealer == other.dealer
            and
            self._cards == other._cards
        )

