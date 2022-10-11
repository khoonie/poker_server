class Card:
    RANKS = {
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "J",
        12: "Q",
        13: "K",
        14: "A",
    }
    SUITS = {
        3: u"\u2665", # Heart
        2: u"\u2666", # Diamond
        1: u"\u2663", # Club
        0: u"\u2660", # Spade
    }

    def __init__(self, rank: int, suit: int):
        if rank not in Card.RANKS:
            raise ValueError("Invalid card rank")
        if suit not in Card.SUITS:
            raise ValueError("Invalid card suit")
        self._value: int = (rank << 2) + suit

    def rank(self) -> int:
        return self._value >> 2

    def suit(self) -> int:
        return self._value & 3

    def __lt__(self, other):
        return int(self) < int(other)

    def __eq__(self, other):
        return int(self) == int(other)

    def __int__(self):
        return self._value

    def dto(self):
        return self.rank, self.suit