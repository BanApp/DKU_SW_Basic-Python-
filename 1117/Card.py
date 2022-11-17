class Card:
    suitNames = ['클로버','다이아몬드','하트','스페이드']
    rankNames = [None,'에이스'] + [str(i) for i in range(2,11)] + ['잭','퀸','킹']

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return Card.suitNames[self.suit] +" " +Card.rankNames[self.rank]

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)

    def __str__(self):
        lst = [str(card) for card in self.cards]
        return str(lst)

deck = Deck()
print(deck)
