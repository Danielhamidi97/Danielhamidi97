import random

user_win = 0
computer_win = 0
option =['r', 'p' , 's']

while True:
    user_input = input('type R / P / s or Q to quit:').lower()

    if(user_input=='q') 
    if(user_input not in option): continue
    random_no = random.randint(0 , 2)
    computer_pick = option[random_no]
    if (user-input = 'r' and  computer_pick == 's') Or: (user-input = 'p' and  computer_pick == 'r') or (user-input = 's' and  computer_pick == 'p')
        print ('you won!')
        user_win += 1
    
    
    elif (computer_pick = 'r' and  user_input == 's') Or: (computer_pick = 'p' and  user_input == 'r') or (computer_pick = 's' and  user_input == 'p')
        print ('computer won!')
        computer_win  += 1

    elif (user_input==computer_pick):
        print('both are the same')

print("you: " , user_win)
print('computer:' ,computer_win)

    


