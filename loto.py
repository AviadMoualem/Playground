
import random

# input example - 1,5,6

def is_number_exist_in_arr(n, arr):
    exist = False
    for p in arr:
        if int(n) == int(p):
            exist = True
            break

    return exist

print("This is a loto game!")


attepts = 0
con = True
while (con):

    attepts = attepts + 1
    print("This is your attempt number: ",attepts)
    nums = input("Please enter 3 numbers from 0 to 9 comma separeated \n")
    arr = nums.split(",") # [1,5,6]
    arr_rnd = []

    # random numbers
    for i in range(3):
        rand = random.randint(0, 9)
        while ( len(arr_rnd) > 0 and is_number_exist_in_arr(rand, arr_rnd)):
            rand = random.randint(0, 9)
        arr_rnd.append(rand)

    print("Random numbers: ",arr_rnd)

    # check winner 
    flag = True
    for n in arr:
        if flag == True:
            if not is_number_exist_in_arr(n, arr_rnd):
                flag = False
        else:
          break

    if flag == True:
        print("You win!")
    else:
        print("You lose!")
    
    kelet = input("Do you want to continue? Y|N \n")
    if kelet.lower() == 'y':
        con = True
    else:
        con = False