cards = input().split()
count_shuffles = int(input())

for shuffle in range(count_shuffles):
    final_deck_list = []
    middle_deck = len(cards) // 2
    left_side = cards[:middle_deck]
    right_side = cards[middle_deck:]
    for card in range(len(left_side)):
        final_deck_list.append(left_side[card])
        final_deck_list.append(right_side[card])
    cards = final_deck_list
print(cards)




# Task:
# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half.
# Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still on the bottom and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives a count of faro shuffles that should be made. Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.