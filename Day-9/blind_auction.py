import art

print(art.logo)
bids = {}
flag = False


def find_highest_bidder(bidding_record):
    highest_price = 0
    highest_name = ""
    for bids1 in bidding_record:
        if highest_price < bidding_record[bids1]:
            highest_price = bidding_record[bids1]
            highest_name = bids1
    print(f"The winner is {highest_name} with a bid of {highest_price}")


while not flag:
    print("What is you name?")
    name = input()
    print("What's your bid?")
    price = int(input())

    bids[name] = price

    print("Are there any other bidders? Type 'yes or 'no'.")
    should_continue = input()
    if should_continue == "no":
        flag = True
        find_highest_bidder(bids)
    else:
        pass