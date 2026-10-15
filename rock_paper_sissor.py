first_player= input("Enter the first action: ")
second_player = input("Enter the second player action: ")
if first_player == 'rock':
    if second_player == 'sissor':
        print('Fist Won')
    else:
        print('Second Won')
elif first_player == 'paper':
    if second_player == 'sissor':
        print('second won')
    else:
        print('first won')
elif first_player == 'sissor':
    if second_player == 'stone':
        print('second won')
    else:
        print('first won')
else:
    print("invalid input")