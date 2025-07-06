import random, sys

     
kbc = "WELCOME TO KOUN BANEGA CROCER PATI"
print(kbc.center(100))

questions =[
    ["1.Which language is used to make fb?\n",
     "php", "python", "JavaScrip", "matlab",1
    ],
    ["2.In which year Python language was developed?\n",
     "1980", "1990", "1991", "2001",3
    ],
    ["3.Python was developed in which country?\n",
     "Germany", "Russia", "Natherland", "USA",3
    ],
    ["4.Who create Python lnaguage?\n",
     "Guido van Rossum", "Robat Browni", "Hamiltonial", "Mosco venchi",1
    ],
    [
    "5.What was the Python language first version?\n",
     "Python 3.08", "Python 0.9.0", "Python 3.13.5", "Python 4.82.1",2
    ],
    ["6.What is the output of print(2 + 2 * 3)",
     "12", "8", "10", "7",2
    ],
    ["7. What will be the output of the code x = 'hello'; print(x[1])\n",
     "h", "e", "l", "error",2
    ],
    ["8.What is a variable in Python?\n",
     "A reserved word", "A data type", "A location in memory to store data", "A function",3
    ],
    ["10.How do you declare a variable in Python?\n",
     "var x", "x = variable", "declare x", "x = 4",4
    ],
    ["11..Which of the following data types is immutable in Python?\n",
     "List", "Tuple", "Set", "Dictionary",2
    ],
    ["12.What does the type() function return in Python?\n",
     "The value of the variable", "The type of the variable", "The memory address of the variable", "The length of the variable",2
    ],
   
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000]
money = 0
lifeline_available = True

def quit_game():
    print(f"\n🛑🛑 You chose to quit the game.\n🏆 You take home Rs.{money}.")
    sys.exit()

for i in range(0,len(questions)):
    question = questions[i]

    print(f"Qestion for money RS.{levels[i]: }\n")

    print(question[0])

    print(f"1.{question[1]}      2.{question[2]}        3.{question[3]}       4.{question[4]}\n")


    reply = int(input("Enter you Choice(1-4) or 0 to quit or 9 to acive 50-50 lifeline:  "))

    if reply in (0,'quit'):
        quit_game()
    
    if reply in (9, 'lifeline'):
        if lifeline_available: 
            lifeline_available = False
            correct_index = question[-1]
            # pick two wrong anser to hide
            wrong = [i for i in range(1,5) if i != correct_index]
            to_remove= random.sample(wrong,2)
            
            print("50-50 lifeline used! Two wrong options removed\n")

            for opt in range(1, 5):
                if opt not in to_remove:          
                     print(f"{opt}. {question[opt]}") 
            
            reply = int(input("your choice (1-4) or 0 to quit: "))
            if reply in ('q', 'quit', 0):
                quit_game()
            

        else:

            print("❌ Lifeline already used.")
            # 
            while True:
                reply = int(input("Enter 1-4 or 0 to quit: "))
                if reply in (0, 'quit'):
                    quit_game()
                    
                if reply in [1,2,3,4]:
                    break
                print("⚠️  Invalid choice, try again.")
                sys.exit()


    if reply not in[1,2,3,4]:
        print("Invalid input, Try again.\n")
        break
   
   
    if reply == question[-1]:
        money = levels[i]
        print(f"🎉 Correct! You have won Rs.{levels[i]}\n")
        
    else:
        print("❌ Sorry Wrong answer\n")

print(f"\n🏆 You take home Rs.{money}. Congratulations!")

    







