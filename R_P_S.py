import random

while True:
    print("1.Rock,2.Paper,3.scissor")
    user_input = int(input("Enter the no: "))

    while user_input > 3 or user_input < 1:
        user_input = int(input("please enter the no.(1-3)"))
        break
    
    if user_input == 1:
        user_input_choice = "Rock"
    elif user_input == 2:
        user_input_choice = "Paper"
    else:
        user_input_choice = "Scissor"
    print("You selected",user_input_choice)

    device_choice = random.randint(1,3)

    while user_input == device_choice:
        device_choice = random.randint(1,3)
    
    if device_choice == 1:
        device_input_choice = "Rock"
    elif device_choice == 2:
        device_input_choice = "Paper"
    else:
        device_input_choice = "Scissor"
    print("Device selected",device_input_choice)


    if ((user_input == 1 and device_choice == 2) or (user_input == 2 and device_choice == 1)):
        print("Paper wins in this situation")
        result = "Paper"
    elif ((user_input == 2 and device_choice == 3) or (user_input == 3 and device_choice == 2)):
        print("Scissor wins in this situation")
        result = "Scissor"
    else:
        print("Rock wins in this situation")
        result = "Rock"

    if user_input_choice == result:
        print("---------------------")
        print("You Win")
    else:
        print("---------------------")
        print("Device Win")
        print("---------------------")
