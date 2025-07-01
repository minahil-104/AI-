#Q:8 Profit or Loss 
def calculate_profit_or_loss(cp, sp):
    if sp > cp:
        profit = sp - cp
        print("Profit of ", profit)
    elif sp < cp:
        loss = cp - sp
        print("Loss of",loss)
    else:
        print("No Profit No Loss")

# Taking input from user
cp = float(input("Enter Cost Price (CP): "))
sp = float(input("Enter Selling Price (SP): "))

# Calling the function
calculate_profit_or_loss(cp, sp)
