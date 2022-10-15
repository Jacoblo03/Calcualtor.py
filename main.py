
#define the functions needed: add, mult, sub, div
def add(a,b):
    answer = a + b 
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a,b):
    answer = a - b 
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mult(a,b):
    answer = a * b 
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a,b):
    answer = a / b 
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")


while True:
    def calc():
    
        print("A. Addition")
        print("B. Subtraction")
        print("C. Multiplication")
        print("C. Division")
        print()

        #ask for values
        choice = input("Please input your choice: ")
        if choice == 'a' or choice == 'A':
            ("Addition")
            a = int(input("Input your first number: "))
            b = int(input("Input your second number: "))
            add(a,b)
        elif choice == 'b' or choice == 'B':
            ("Subtraction")
            a = int(input("Input your first number: "))
            b = int(input("Input your second number: "))
            sub(a,b)
        elif choice == 'c' or choice == 'C':
            print("Multiplication")
            a = int(input("Input your first number: "))
            b = int(input("Input your second number: "))
            mult(a,b)
        elif choice == 'd' or choice == 'D':
            ("Division")
            a = int(input("Input your first number: "))
            b = int(input("Input your second number: "))
            div(a,b)
    calc()

    #ask user if they want to play again
    def play_again():
        play_again = input("Would you like to play again? y/n: ")
        if play_again == 'y' or play_again == 'Y':
            calc()
        else:
            play_again == 'n' or play_again == 'N'
            print('Thanks for playing!')
    play_again()
    break