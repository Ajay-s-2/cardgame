import random
cards =[]
suits =["spades","hearts","diamonds","clubs"]
rank =[ "A","2","3","4","5","6","7","8","9","10","J","Q","K"]

for suit in suits:
    for ranks in rank:
        cards.append([suit,rank])

print(cards)