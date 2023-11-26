print ("Hello, this is cool average app")
print ("Please enter numbers")

flag = True
sum = 0
counter = 0
while flag:
    kelet = input()
    if kelet == 'q':
        flag = False
    else:
        num = int(kelet)
        sum = sum + num
        counter = counter + 1

average = sum / counter
print ('The average is: ', average)

