def main():
    cokePrice = 50
    coin = 0
    amountDue = 0
    drop = 0

    while cokePrice > coin:
        drop = input("Insert Coin: ")
        drop = drop.strip()
        
        try:
            drop = int(drop)
            if(drop in [5, 10, 25]):
                coin += drop
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        amountDue = cokePrice - coin
        
        if amountDue >0 :
            print("Amount Due: ", amountDue, sep = "")

    print("Change Owed: ", amountDue * -1, sep='')


main()