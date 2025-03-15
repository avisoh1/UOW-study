import random    

class Card:
    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value
    
    def getSuit(self):
        return self.__suit

    def getValue(self):
        return self.__value
    
    def isBigger(self, anotherCard):
        suitRank = ("Diamond","Club","Heart","Spade")
        valueRank = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')
        if valueRank.index(self.getValue()) > valueRank.index(anotherCard.getValue()):
            return True
        elif valueRank.index(self.getValue()) < valueRank.index(anotherCard.getValue()):
            return False
        elif suitRank.index(self.getSuit()) > suitRank.index(anotherCard.getSuit()): # equal value
            return True
        else:
            return False

    def __str__(self):
        return self.__value + ' of ' + self.__suit

class Deck:
    def __init__(self):
        suit = ['Spade','Heart','Diamond','Club']
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.__cards = [  ]
        for s in suit:
            for v in values:
                self.__cards.append(Card(s, v))

    def shuffle(self):
        random.shuffle(self.__cards)

    def dealCard(self):
        return self.__cards.pop()    

    def __str__(self):
        text = ""
        for c in self.__cards:
            text += str(c) + "\n"
        return text
    
def main():
    d = Deck()
    d.shuffle()
    print(d)
   
    p1,p2 = 0,0
    while True:
        p1Card = d.dealCard()
        p2Card = d.dealCard()
        print("Player 1 : {}".format(p1Card))
        print("Player 2 : {}".format(p2Card))
        if p1Card.isBigger(p2Card):
            print("Player 1 wins")
            p1 += 1
        else:
            print("Player 2 wins")
            p2 += 1
            
        if p1 > 2:
            print("P1 is overall winner!!")
            break
        elif p2 > 2:
            print("P2 is overall winner!!")
            break


main()

