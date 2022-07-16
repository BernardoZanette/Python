import string
from time import sleep
noteA = noteB = noteC = noteD = noteE = 0
notes_list = []
ave = 0
print('\t Cinema evaluation\t\n')
sleep(1)
print('\t  Notes | Meaning')
sleep(0.5)
print('\t ' +'-'*17)
sleep(0.5)
print('\t   A   | Very good')
sleep(0.5)
print('\t ' +'-'*17)
sleep(0.5)
print('\t   B   | Good')
sleep(0.5)
print('\t ' +'-'*17)
sleep(0.5)
print('\t   C   | Regular')
sleep(0.5)
print('\t ' +'-'*17)
sleep(0.5)
print('\t   D   | Bad')
sleep(0.5)
print('\t ' +'-'*17)
sleep(0.5)
print('\t   E   | Very bad\n\n')
people = int(input('How many people will evaluate the film? '))
for c in range (0,people):
    age = int(input('Age: '))
    if (age < 0 or age > 100):
        print('Come on.')
    else:
        ave = age + ave
    note = str(input('Note: '))
    print('-'*20)
    ofnote = note[0].upper()
    if (ofnote == 'A'):
        noteA += 1
    elif (ofnote == 'B'):
        noteB += 1
    elif (ofnote == 'C'):
        noteC += 1
    elif (ofnote == 'D'):
        noteD += 1
    elif (ofnote == 'E'):
        noteE += 1
    else: 
        print('Please enter with a letter from A to E.')
print(f'The ages avarage: {round(ave/people, 2)}')
print(f'Percentage A note: {round(noteA*100/people, 2)}')
print(f'Percentage B note: {round(noteB*100/people, 2)}')
print(f'Percentage C note: {round(noteC*100/people, 2)}')
print(f'Percentage D note: {round(noteD*100/people, 2)}')
print(f'Percentage E note: {round(noteE*100/people, 2)}')