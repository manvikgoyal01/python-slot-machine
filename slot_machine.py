import sys
import math
import random
import pandas as pd

MIN_LINES=1 #minimum number of lines/rows in slot machine, not same as lines chosen by the user
MAX_LINES=3 #maximum number of lines/rows in slot machine, not same as lines chosen by the user
MAX_COLS=3 #total number of columns/reels in the slot machine
MIN_BET=1 #(per line)
MAX_BET=100 #(perline)
SYMBOL_COUNT={"A":2,"B":4,"C":6,"D":8} #Number of times each symbol appears in the symbol pool (affects randomness)
SYMBOL_VALUE={"A":5,"B":4,"C":3,"D":2} #Payout multiplier for each symbol if matched across a winning line

#creates a symbol pool to select from
SYMBOL_LIST=[]
for x,y in SYMBOL_COUNT.items():
    for _ in range(y):
        SYMBOL_LIST.append(x)
    
    
#asks the user to deposit a valid amount 
def get_deposited():
    while True:
        try:
            dep=int(input("Enter the amount to deposit : $"))
            if dep>0:
                break
            else:
                print("Please deposit at least $1.\n")
        except ValueError:
            print("The amount should be a number (alteast $1).\n")
    return dep


#asks the user for valid no. of lines to bet on
def get_lines(balance):
    while True:
        try:
            line=int(input(f"Enter the number of lines to bet ({MIN_LINES} - {MAX_LINES}) : "))
            if MIN_LINES <= line <= MAX_LINES :
                if balance >= MIN_BET*line:
                    break
                else:
                    print(f"You do not have enough balance to bet on {line} lines. You can bet on {math.floor(balance/MIN_BET)} lines at maximum.\n ")
            else:
                print(f"You can only choose from {MIN_LINES} to {MAX_LINES} lines to bet on. \n")
        except ValueError:
            print(f"The lines to bet on must be a number from {MIN_LINES} to {MAX_LINES}. \n")
    return line


#asks a valid amount to bet on each line
def get_bet(lines,balance):
    while True:
        try:
            bet=int(input("Enter the amount to bet (per line) : $"))
            if MAX_BET >= bet >= MIN_BET and balance>= bet*lines :
                break
            elif balance < bet*lines:
                print(f"You do not have enough balance to bet ${bet} on {lines} lines. You can bet on ${math.floor(balance/lines)} on each line.\n ")
            else:
                print(f"Your bet must be from ${MIN_BET} to ${MAX_BET} (per line).\n")
        except ValueError:
            print(f"The amount should be a number from ${MIN_BET} to ${MAX_BET}. \n")
    return bet


#asks for user's confirmation
def consent(bet,lines,balance):
    while True:
        cons=input(f"Are you sure you want to bet ${bet} on {lines} lines, for a total of ${bet*lines}? You have ${balance} left. (Y/N/Q) :").strip().upper()
        print()
        if cons=='Y':
            break
        elif cons=='Q':
            print("Thank you for playing!")
            sys.exit()
        elif cons=='N':
            lines=get_lines(balance)
            bet=get_bet(lines, balance)
        else:
            print("Please choose from Y/N/Q.")
    return(lines,bet)


#one spin of the game
def spin(lines,bet):
    
    winnings = 0
    
    #choses the values of each cell
    spindata=pd.DataFrame()
    for j in range(MAX_COLS):
        symbol_list=SYMBOL_LIST[:]
        for i in range(MAX_LINES):
            roll = random.choice(symbol_list)
            spindata.at[i,j] = roll
            symbol_list.remove(roll)
     
    #creating name for index and columns
    col_names=[f"Col {i+1}" for i in range(MAX_COLS)]
    indexes= [f"Line {i+1}" for i in range(MAX_LINES)]
    spindata.index=indexes
    spindata.columns=col_names
     
       
    print(spindata)
    
    #processing of the win status, line by line
    for i in range(MAX_LINES):
        win=True
        
        if i <= lines-1 :  
            for j in range(MAX_COLS):
               if spindata.iloc[i,j] != spindata.iloc[i,0]:
                   win=False
                   break
            
             #calculating winnings and informing the user
            if win:
                winnings += SYMBOL_VALUE[spindata.iloc[i,0]]*bet
                print(f"You won ${SYMBOL_VALUE[spindata.iloc[i,0]]*bet} on line {i+1}.")
            else :
                print(f"You lost on line {i+1}")
                        
        else:
            print(f"You did not bet on line {i+1}.")
        
    return winnings

                
# Handles deposit, betting, spinning, and balance updates
# Tracks total winnings and number of spins
# Repeats as long as user wants to continue and has enough balance
def main():
    spin_count=0
    total_winnings=0
    
    balance=get_deposited()
    
    while True:
        spin_count += 1
        
        obalance = balance 
        
        lines=get_lines(balance)
        bet=get_bet(lines, balance)
        lines,bet=consent(bet, lines, balance)
        winnings=spin(lines, bet)
        
        balance += - bet*lines + winnings
        total_winnings += winnings
        
        print(f"\n Spin #{spin_count} Results : \n")
        print(f"Spin Winnings : ${winnings}")
        print(f"Total Winnings ${total_winnings}")
        print(f"Updated Balance : ${balance}")
        print(f"Change in Balance : ${balance-obalance} \n")
        
        
        #asking if the user wants to continue the game (and checking minimum balance needed)
        while True: 
            
            if balance >= MIN_BET:
                choice=input("Would you like to continue the game (Y/N)? ").strip().upper()
            else:
                print(f"You need minimum ${MIN_BET} to continue. Your current balance is only ${balance}.")
                choice=input("Would you like to continue the game by depositing more money (Y/N)? ").strip().upper()
                
            if choice == 'Y':
                print("\n Continuing the Game! \n")
                break
            elif choice in ['N','Q']:
                print("\n Thank You for playing! \n")
                sys.exit()
            else:
                print("Please choose Y or N!")
                
                
        #asking whether the user wants to deposit more money       
        while True:     
            if balance >= MIN_BET:
                choice=input("Would you like to deposit more money (Y/N/Q)? ").strip().upper()
            else:
                choice='Y'
                
            if choice == 'Y':
                balance += get_deposited()
                break
            elif choice=='N':
                break
            elif choice=='Q':
                sys.exit()
            else:
                print("Please choose Y or N!")
            
main()
