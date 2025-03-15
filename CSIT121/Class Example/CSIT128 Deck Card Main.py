import random
        
def main():
    deck = []
    suitRank = ("Diamond","Club","Heart","Spade")
    valueRank = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')
    for s in suitRank:
        for v in valueRank:
            deck.append((s, v))
    
    random.shuffle(deck)
    p1,p2 = 0,0
    while True:
        card1 = deck.pop()
        card2 = deck.pop()
        print("Player 1 : {}".format(card1))
        print("Player 2 : {}".format(card2))
        
        if valueRank.index(card1[1]) > valueRank.index(card2[1]):
            print("Player 1 wins")
            p1 += 1
        elif valueRank.index(card1[1]) < valueRank.index(card2[1]):
            print("Player 2 wins")
            p2 += 1
        elif suitRank.index(card1[0]) > suitRank.index(card2[0]): 
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





