# write a program to print a number of options and allow the user to select
# an option from the list.
# the options should be numbered from 1-9 (minimum 4)
# the program should continue looping, allowing the user to choose one
# of the options each time around. the loop should only terminate when
# the user chooses 0. if the user makes a valid choice, the program should
# print a short message. the message should include the value that they
# typed. As an optional extra, modify the program so that the menu
# is printed again, if the user chooses an invalid option

choice = None

while choice != 0:
    print("Please pick an option: \n"
          "1. Run \n"
          "2. Jump \n"
          "3. Climb \n"
          "4. Fly \n"
          "5. Exit")
    choice = int(input("What number? ->"))
    if choice in range(0, 4):
        print("You picked {}".format(choice))
    elif choice == 5:
        break
    else:
        print("Invalid option")

