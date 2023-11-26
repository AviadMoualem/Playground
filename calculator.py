print (">> hello world I am Aviad")
print (">> I am the king goat")

name = input('>> What is your name?\n')    
print(">> Hello "  + name)

num = input('>> Please enter a number and I am multiply by 2\n')
print('>> The result is:')
result= int(num) * 2
print(result)


numAttempts = 2
print ("This is Aviad's calculator")
# print ('you have ' + str(numAttempts) + ' attempts')
keepCalc = True 
i =0
while keepCalc:
    print('attempt number ',i+1)
    num1 = int((input)('>> please enter first number\n'))
    num2 = int((input)('>> please enter second number\n'))
    oper = input ('>> please enter operator\n')
    if oper == '+':
        res = num1 + num2
    elif oper == '*':
        res = num1 * num2
    elif oper == ':':
        res = num1/num2
    elif oper == '-':
        res = num1 - num2

    print('>> the answer is: \n', res)
    i+=1
    cnt = input('>> do you want to continue? Y|N \n')
    if cnt == 'N':
        keepCalc = False
    # if i == numAttempts:
    #     keepCalc = False


print('>>Bye:)')