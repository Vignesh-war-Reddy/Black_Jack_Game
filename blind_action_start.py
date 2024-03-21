import os
bids = {}
bidding_finished = False
print("Welcome to the blind_action bidding")

def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winneris {winner} with a bid mount of ${highest_bid}")

    
while not bidding_finished:
    name = input(" What is ur name hgfd")
    price = int(input("what is ur bid? $"))
    bids[name] = price
    should_continue = input("Are there any other biding ? 'yes' or 'no'.")
    os.system('clear')
    if should_continue == "no":
        bidding_finished = True
        find_highest_bid(bids)
        
        

