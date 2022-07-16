result = 0
list_n = []
list_fac = []
n_quest = int(input('Enter a number of questions: '))
if (n_quest < 0):
    print('\nCome on.')
else:
    for c in range(0,n_quest):
        n = int(input('Enter a number: '))
        if (n <= 0):
            print('-'*44)
            print('Please, enter a positive and integer number')
            print('-'*44)
        else:
            list_n.append(n)
            result = n
            factorial = 1
            while (factorial < n):
                result = result*factorial
                factorial += 1
            list_fac.append(result)
    print (f'The numbers you entered: {list_n}')
    print (f'The respectives factorials: {list_fac}')