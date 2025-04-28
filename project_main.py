import random

robber_money = 100
car = 0
mask = 0 
bow_and_arrow = 0
roll_history = []

#comment from chu ti
def shop():
    global robber_money
    global car
    global mask
    global bow_and_arrow
    
    while True:
        item_selection = input(f"What would you like to buy? Enter 'X' to leave shop. You have ${robber_money} \n car ($350) \n mask ($20) \n bow and arrow ($50)\n")
        if item_selection == "car":
            if robber_money - 350 < 0: 
                print(f"You don't have enough money for this. \nYour balance is ${robber_money}")
                print("----------")
            else:
                robber_money -= 350
                car += 1
                print(f"You bought a car. \nYour balance is ${robber_money}")
                print("----------")
        elif item_selection == "mask":
            if robber_money - 20 < 0:
                print(f"You don't have enough money for this.\nYour balance is ${robber_money}")
                print("----------")
            else:
                robber_money -= 20
                print(f"You bought a mask. \nYour updated balance is ${robber_money}")
                print("----------")
                mask += 1
        elif item_selection == "bow and arrow":
            if robber_money - 50 < 0: 
                print(f"You don't have enough money for this. \nYour balance is ${robber_money}")
                print("----------")
            else:
                robber_money -= 50
                print(f"You bought a bow and arrow. \nYour updated balance is ${robber_money}")
                print("----------")
                bow_and_arrow += 1
        elif item_selection == "X":
            show_robber_options()
            break 
        else:
            print("Please enter a valid answer.")
            print("----------")


def rob_bank(): 
    global robber_money
    global roll_history
    
    dice_char = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    total_points = car * 10 + mask * 2 + bow_and_arrow * 5

    print("-----------")
    while True:    
        user_input = input("Enter 'roll' to roll the dice. 'X' to leave.\n")
        if user_input == "roll":
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            
            final_value = die1 + die2

            die1 = dice_char[die1 - 1]
            die2 = dice_char[die2 - 1]

            count = 1

            if final_value == 7:
                print(f"You rolled {die1} and {die2}, which adds to 7 (you got caught by police). GAME OVER.")
                print("------------")
                print("TOTAL POINTS EARNED:")
                print(f" {total_points} points")
                print("STATS:")
                print(f" You bought {car} cars, {mask} masks, and {bow_and_arrow} bow and arrows.")
                roll_history.append(str(final_value))
                print("DICE ROLL HISTORY:")
                for roll in roll_history:
                    print(f" roll {count}: {roll}")
                    count += 1
                print("----------")
                print("Thanks for playing!")
                exit()
            else:
                money_added = final_value * 10
                print(f"You rolled {die1} and {die2}, which adds to {final_value}. You gained ${money_added}.\n----------")
                robber_money += money_added
                roll_history.append(final_value)
        elif user_input == "X":
            show_robber_options()
            break
        else:
            print("Please select a valid answer.")

def show_robber_options(name):
    print("----------")
    while True:    
        selected_option = input(f"Hello {name}! You are a robber. What would you like to do? \n rob bank\n buy weapons \n view items\n more info\n")
        if selected_option == "rob bank":
            rob_bank()
        elif selected_option == "buy weapons":
            print("----------")
            print("Welcome to the shop!")
            shop()
        elif selected_option == "view items":
            print("----------")
            print(f"You have: \n {car} cars \n {mask} masks \n {bow_and_arrow} bow and arrows")
            print("----------")
        elif selected_option == "more info":
            print("\nThe objective of this game is simple, rob banks to buy as much items as possible.")
            print("The more items you buy, the more points you get.")
            print("To rob banks, you must roll a set of dice. Rolling a 7 would end the game.\n-----------")
        else:
            print("----------\nPlease select a valid option.")
    

name = input("What is your name? ")

print("The objective of this game is simple, rob banks to buy as much items as possible.")
print("The more items you buy, the more points you get.")
print("To rob banks, you must roll a set of dice. Rolling a 7 would end the game.\n")
show_robber_options()

