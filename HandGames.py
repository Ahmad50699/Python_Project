import random

class RPS:
    def __init__(self):
        self.moves =["Rock","Paper","Scissor"]
    def play(self):
        user = input("Enter your move [Rock, Paper, Scissor]: ").capitalize()
        computer = random.choice(self.moves)
        print(f"USER: {user}, COMPUETR: {computer}")
        
        if user == computer:
            print("TIE!!")
        elif (user == "Rock" and computer == "Scissor") or (user == "Paper" and computer == "Rock") or (user == "Scissor" and computer == "Paper"):
            print("USER WIN!!!!")
        elif user in self.moves:
            print("COMPUTER WIN!!!")
        else:
            print("Move correctly")

class HeadTails:
    def toss(self):
        print("\n TOSS THE COIN")
        user_toss = input("Choose Head OR Tails: ").capitalize()
        user_number = int(input("Choose Number from 1-5: "))
        computer_number = random.randint(1, 5)
        total = user_number + computer_number
        result = "Head" if total % 2 != 0 else "Tails"
        print(f"User Number: {user_number}, Computer Number:{computer_number}")
        print(f"{total}, So {result} Wins!")

        if user_toss == result:
            print("User Won The Toss!!")
            choose = input("Bat or Bowl: ").capitalize()
            return choose
        else:
            print("Computer Won The Toss!")
            computer_choose= random.choice(["Bat", "Bowl"])
            print(f"Computer chooses to {computer_choose}")
            return "Bat" if computer_choose == "Bowl" else "Bowl"
       
    def play(self):
        role = self.toss()
        target = random.randint(1, 50)
        print(f"Target = {target}")
        score = 0
        print("\n GAME START")

        while True:
            user_run = int(input ("Hit your Shots!!!(0-6): "))
            if user_run not in range(0, 7):
                print("Invalid run! Enter 0-6 only.")
                continue

            computer_run = random.randint(0, 6)
            print (f"Computer: {computer_run}")

            if user_run == computer_run:
               print("Ohh no! You are OUT")
               if score >= target:
                   print("User Win The Match")
               else:
                   print("Lose the game")
               break

               
            else:
               score += user_run
               print(f"Score = {score}")
         
while True:
    print("\n Choose the game you want to play:")
    print("1. Rock Paper Scissors")
    print("2. Head-Tails[Hand Cricket]")
    choice = input("Select the game: ")
    if choice == "1":
        game1 = RPS()
        game1.play()
    elif choice == "2":
        game2 = HeadTails()
        game2.play()



