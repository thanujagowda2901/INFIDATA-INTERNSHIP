print('select a food category 1:veg,2:non_veg')
choice = int(input('select ur choice'))
if (choice == 1):
    print('you have selected veg category')
    menu = int(input('select menu 1:meals 2:idli 3:dosa'))
    if (menu == 1):
        print('you have selected meals')
    elif (menu == 2):
        print('you have selected idli')
    elif (menu == 3):
        print('you have selected dosa')
    else:
        print('menu not available')
elif(choice==2):
    print('you have selected non veg')
    menu = int(input('select menu 4:fish 5:prawn 6:biriyani'))
    if (menu == 4):
        print('you have selected fish')
    elif (menu == 5):
        print('you have selected prawn')
    elif (menu == 6):
        print('you have selected biriyani')
    else:
        print('menu not available')
else:
    print('invalid category ')
