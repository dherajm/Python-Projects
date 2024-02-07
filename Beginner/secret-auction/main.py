import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

auction_details = []
bids = []


def auctioneer_details():
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    auction_details.append({"name": name, "bid": bid})


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def compare_bids(auction_details):
    highest_bid = max(auction_details, key=lambda x: x["bid"])
    return highest_bid


def main():
    while True:
        auctioneer_details()
        
        cont = input("Is there another bidder? 'yes' or 'no'\n")
        
        if cont.lower() == 'no':
            clear()
            break
        else:
            clear()
    
    highest_bidder = compare_bids(auction_details)
          
    print(f"Highest bidder is {highest_bidder['name']} with a bid of ${highest_bidder['bid']}")

if __name__ == '__main__':
    main()
