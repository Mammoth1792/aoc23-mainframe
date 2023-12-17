def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        if i == 1:
            continue
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num

# Read in list of hands
list_of_hands = []
with open("input.txt") as f:
    for line in f:
       (hand, bid) = line.split()
       hand_bid_dict = {}
       hand_bid_dict["hand"] = hand
       hand_bid_dict["bid"] = int(bid)
       list_of_hands.append(hand_bid_dict)

for hand in range(len(list_of_hands)):
    cards_in_hand = [*list_of_hands[hand]["hand"]]
    for card in range(len(cards_in_hand)):
        match cards_in_hand[card]:
            case "T":
                cards_in_hand[card] = 10
            case "J":
                cards_in_hand[card] = 1 # Joker strengh is 1
            case "Q":
                cards_in_hand[card] = 12
            case "K":
                cards_in_hand[card] = 13
            case "A":
                cards_in_hand[card] = 14
            case _:
                cards_in_hand[card] = int(cards_in_hand[card])
    list_of_hands[hand]["hand"] = cards_in_hand
    num_of_jokers = cards_in_hand.count(1)
    modified_hand = cards_in_hand
    if num_of_jokers:  # If there's a Joker...
        card_to_replace = most_frequent(cards_in_hand)
        modified_hand = [card_to_replace if card == 1 
                                                else card for card in cards_in_hand]
    set_of_cards = set(modified_hand)
    match len(set_of_cards):
        case 1:
            hand_rank = 7 # Five of a Kind
        case 2:
            hand_rank = 5 # Full House unless...
            for card in set_of_cards:
                count = modified_hand.count(card)
                if count == 1:
                    hand_rank = 6 #...we find Four of a Kind
        case 3:
            hand_rank = 3 # Two Pair unless...
            for card in set_of_cards:
                count = modified_hand.count(card)
                if count == 3:
                    hand_rank = 4 #...we find Three of a Kind
        case 4:
            hand_rank = 2
        case 5:
            hand_rank = 1
    list_of_hands[hand]["hand_rank"] = hand_rank
sorted_list_of_hands = sorted(list_of_hands, key = lambda x: 
                              (x["hand_rank"], x["hand"][0], x["hand"][1], 
                               x["hand"][2], x["hand"][3], x["hand"][4]))

rank = 1
total = 0
for hand in range(len(sorted_list_of_hands)):
    total_bid = sorted_list_of_hands[hand]["bid"] * rank
    total += total_bid
    rank += 1

print(total)
