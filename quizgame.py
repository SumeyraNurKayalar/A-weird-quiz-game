print("Welcome to the computer quiz")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    print("Okay, maybe next time.")
else:
    print("Game starts then")
    
    answer = input("What's the CPU stands for? ")
    if answer.lower == "central proccesing unit":
        print("correct")
        score += 10
    else:
        print("incorrect")
        
    answer = input("What's the GPU stands for? ")
    if answer.lower == "graphics proccesing unit":
        print("correct")
        score += 10
    else:
        print("incorrect")
        
    answer = input("What does RAM stands for? ")
    if answer.lower == "random access memory":
        print("correct")
        score += 10
    else:
        print("incorrect")
        
    answer = input("What does PSU stands for? ")
    if answer.lower == "power supply":
        print("correct")
        score += 10
    else:
        print("incorrect")
        
    print("You got" + str(score) + "questions correct.")
    print("You got" + str((score / 4) * 100) + "%.")
        
