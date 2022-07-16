validator = 0
n = int(input('Enter a number: '))
for c in range(2,n):
    if (n % c == 0):
        validator = validator + 1
if (n == 1):
    print('1 is not consider a prime number.')
if (validator >= 1):
    print('Not prime.')
else:
    print('Prime.')