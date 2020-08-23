import collections
from random import choice

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spides diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank,suit) for suit in self.suits
                                      for rank in self.ranks]
    def __len__(self):
        return len(self.cards)

    def __getitem__(self,position):
        return self.cards[position]

    def randomize_deck(self):
        new_deck = []

        while len(new_deck) != len(self.cards):
            x = choice(self.cards)
            if x not in new_deck:
                new_deck.append(x)

        return new_deck

deck = FrenchDeck()

#print(deck[50])
#print(len(deck))
#print(choice(deck))
#print(deck[40:52])
'''
for card in deck:
    print(card)

for card in reversed(deck):
    print(card)
'''
#print(Card('Q', 'hearts') in deck)
'''
card_on_deck = []
def deck_pos(deck):

    while True:
        x = choice(deck)
        if x not in card_on_deck:
            card_on_deck.append(x)
        if len(card_on_deck) == 52:
            break
deck_pos(deck)

for card in card_on_deck:
    print(card)

print(len(card_on_deck))
'''
for card in deck.randomize_deck():
    print(card)
