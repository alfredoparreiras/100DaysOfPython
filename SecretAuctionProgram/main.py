bids = {}

print("Welcome to the secret auction program.")
while True:
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: "))
    bids[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no.").lower()
    if other_bidders != "yes":
        break

# Sort bids based on amount
sorted_bids = sorted(bids.items(), key=lambda item: item[1], reverse=True)

print("Bids, from highest to lowest:")
for name, bid in sorted_bids:
    print(f"{name}: {bid}")
