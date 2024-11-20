#project Roulette#
#Casino roulette#



import random 

RED = ['red', 'all red',1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
BLACK = ['black','all black',2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
sin_zero = [0, "zero", 'green']
only_red = RED
only_black = BLACK
even = ['even',0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,20,32,34,36]
odd = ['odd',1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
one_tev = ['1-12', 'one threw twelve']
thirt_twent = ['13-24', 'thirteen threw twenty-four']
twenti_thirty_6 = ['25-36', 'twenty-five threw thirty-six']
chips = 1000


def intro_duction():
    print("Welcome to ULTRA ROULEETE")
    start = input("Do you want to play? ").lower()
    if start != "yes":
        quit()
    else:
        print("Alright, lets get started!")

def rules():
    how = input("Do you need a tutorial on how to play? ").lower()
    if how != "no":
        print("heres how to play ROULETTE!!")
        print("Roulette is a game of chance where players bet on the outcome of a spinning wheel.\n"
              "The game offers various betting options with different odds and payouts.\n"
              "The goal is to correctly predict where the ball will land on the wheel.")
    else:
        print("continue to the game")

def betting(chips):
    while True:
        bet = int(input("Please enter your bet? "))
        if bet > chips:
            print("You do not have enough chips to make that bet. Please enter a lower amount.")
        else:
            break
    
    ### Single Numbers / Single color ###
    single = input("would you like to bet on a single number and square ").lower()
    if single == "yes":
        num = int(input("What number do you want to bet on? "))
        single_color = input("Red Or BLack? ")
        if num and single_color in RED:
            print("You are betting $" + str(bet) + " On " + single_color + " " + str(num))
            cont = input("Do you wish to continue with your bet? ").lower()
            if cont != "yes":
                change = input("Do you want to change your bet amount? ").lower()
                if change == "yes":
                    bet = int(input("Enter your new bet amount! "))
                    print("You are Now betting $" + str(bet) + " On " + single_color + " " + str(num))
        elif num and single_color in BLACK:
            print("You are betting $" + str(bet) + " On " + single_color + " " + str(num))
            cont = input("Do you wish to continue with your bet? ").lower()
            if cont != "yes":
                change = input("Do you want to change your bet amount? ").lower()
                if change == "yes":
                    bet = int(input("Enter your new bet amount! "))
                    print("You are Now betting $" + str(bet) + " On " + single_color + " " + str(num))
    else:
        multi = input("Would you like to bet on multiple squares? ").lower()
        if multi == "yes":
            print("You can bet on all red, all black, all even, all odd, numbers 1 through 12, numbers 13 through 24, numbers 25 through 36, or the number 0.")
            color_num = input("Choose a Color square OR Bet on all red, all black, all even, all odd, numbers 1 through 12, numbers 13 through 24, numbers 25 through 36, or the number 0? ").lower()

        


    ### If user says no with run this instead ###
            if color_num in only_red:
                print("You are betting $" + str(bet) + " on all red.")
                cont = input("Do you wish to continue with your bet? ").lower()
                if cont != "yes":
                    change = input("Do you want to change your bet amount? ").lower()
                    if change == "yes":
                        bet = int(input("Enter your new bet amount! "))
                        print("You are now betting $" + str(bet) + " on all red.")
    
    ### ALL BLACK ###
            elif color_num in only_black:
                print("You are betting $" + str(bet) + " on all black.")
                cont = input("Do you wish to continue with your bet? ").lower()
                if cont != "yes":
                    change = input("Do you want to change your bet amount? ").lower()
                    if change == "yes":
                        bet = int(input("Enter your new bet amount! "))
                        print("You are now betting $" + str(bet) + " on all black.")
    
    ### ALL EVEN ###
            elif color_num == 'all even':
                print("You are betting $" + str(bet) + " on all even numbers.")
                cont = input("Do you wish to continue with your bet? ").lower()
                if cont != "yes":
                    change = input("Do you want to change your bet amount? ").lower()
                    if change == "yes":
                        bet = int(input("Enter your new bet amount! "))
                        print("You are now betting $" + str(bet) + " on all even numbers.")
    
    ### ALL ODD ###
            elif color_num == 'all odd':
                print("You are betting $" + str(bet) + " on all odd numbers.")
                cont = input("Do you wish to continue with your bet? ").lower()
                if cont != "yes":
                    change = input("Do you want to change your bet amount? ").lower()
                    if change == "yes":
                        bet = int(input("Enter your new bet amount! "))
                        print("You are now betting $" + str(bet) + " on all odd numbers.")
    
    ### NUMBERS 1 THROUGH 12 ###
            elif color_num == '1-12':
                print("You are betting $" + str(bet) + " on numbers 1 through 12.")
                cont = input("Do you wish to continue with your bet? ").lower()
                if cont != "yes":
                    change = input("Do you want to change your bet amount? ").lower()
                    if change == "yes":
                        bet = int(input("Enter your new bet amount! "))
                        print("You are now betting $" + str(bet) + " on numbers 1 through 12.")
    
    ### NUMBERS 13 THROUGH 24 ###
            elif color_num == '13-24':
                print("You are betting $" + str(bet) + " on numbers 13 through 24.")
                cont = input("Do you wish to continue with your bet? ").lower()
                if cont != "yes":
                    change = input("Do you want to change your bet amount? ").lower()
                    if change == "yes":
                        bet = int(input("Enter your new bet amount! "))
                        print("You are now betting $" + str(bet) + " on numbers 13 through 24.")
    
    ### NUMBERS 25 THROUGH 36 ###
            elif color_num == '25-36':
                print("You are betting $" + str(bet) + " on numbers 25 through 36.")
                cont = input("Do you wish to continue with your bet? ").lower()
                if cont != "yes":
                    change = input("Do you want to change your bet amount? ").lower()
                    if change == "yes":
                        bet = int(input("Enter your new bet amount! "))
                        print("You are now betting $" + str(bet) + " on numbers 25 through 36.")
    
    ### NUMBER 0 ###
            elif color_num == '0':
                print("You are betting $" + str(bet) + " on the number 0.")
                cont = input("Do you wish to continue with your bet? ").lower()
                if cont != "yes":
                    change = input("Do you want to change your bet amount? ").lower()
                    if change == "yes":
                        bet = int(input("Enter your new bet amount! "))
                        print("You are now betting $" + str(bet) + " on the number 0.")
    
        

    # Simulates the spin
    number, color = spin_wheel()
    print(f"The wheel spun and landed on {number} {color}")
    
    # Check the outcome of the bet
    if single == "yes":
        if number == num and color == single_color:
            print("Congratulations! You won the bet!")
            chips += bet * 35
        else:
            print("Sorry, you lost the bet.")
            chips -= bet
    else:
        if color == 'red' and color_num in RED:
            print("Congratulations! You won the bet!")
            chips += bet  # Payout for a correct color bet
        elif color == 'black' and color_num in BLACK:
            print("Congratulations! You won the bet!")
            chips += bet  # Payout for a correct color bet
        elif number in even and color_num == 'all even':
            print("Congratulations! You won the bet!")
            chips += bet
        elif number in odd and color_num == 'all odd':
            print("Congratulations! You won the bet!")
            chips += bet
        elif number in range(1, 13) and color_num == '1-12':
            print("Congratulations! You won the bet!")
            chips += bet
        elif number in range(13, 25) and color_num == '13-24':
            print("Congratulations! You won the bet!")
            chips += bet
        elif number in range(25, 37) and color_num == '25-36':
            print("Congratulations! You won the bet!")
            chips += bet

        elif number == 0 and color_num == '0':
            print("Congratulations! You won the bet!")
            chips += bet * 35
        else:
            print("Sorry, you lost the bet.")
            chips -= bet
    
    print(f"Your total chips are now ${chips}")
    return chips

### spin Wheel###

def spin_wheel():
    wheel = {
        0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red', 8: 'black', 9: 'red',
        10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red', 15: 'black', 16: 'red', 17: 'black', 18: 'red',
        19: 'red', 20: 'black', 21: 'red', 22: 'black', 23: 'red', 24: 'black', 25: 'red', 26: 'black', 27: 'red',
        28: 'black', 29: 'black', 30: 'red', 31: 'black', 32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'
    }
    number = random.choice(list(wheel.keys()))
    color = wheel[number]
    return number, color

def main_game():
    chips = 1000  # Starting chips for the player
    
    intro_duction()
    rules()
    
    while chips > 0:
        print(f"You have ${chips}")
        chips = betting(chips)
        
        if chips <= 0:
            print("You have run out of chips. Game over!")
            break
        
        cont = input("Do you wish to continue playing? (yes/no): ").lower()
        if cont != "yes":
            break
    
    print(f"You are leaving the game with ${chips}")
    print("Try Again Next Time :) ")

if __name__ == "__main__":
    main_game()


