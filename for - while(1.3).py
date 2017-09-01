for looper in [1, 2, 3, 4, 5]:
    print('hello')
for looper in [1, 2, 3, 4, 5]:
    print(looper)

'''sim = 0
for looper in range(0, 101):
    print(looper, 'умножить на', sim, '=', looper * sim)
    sim += 1'''

'''for letter in range(0, 101, 2):
    print(letter)'''

"""import time
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print('Start')"""

'''i = int(input())
while i != 0:
    print(i)
    i+=1'''

for i in range(0, 6):
    print('---continue---')
    print('i = ', i)
    print('Привет, как ', end='')
    if i == 3:
        continue
    print('твои дела?')

for i in range(0, 6):
    print("---- break ----")
    print('i = ', i)
    print('Привет, как ', end='')
    if i == 3:
        break
    print('твои дела?')

for i in range(1, 6, 2):
    print('Hello, World')

for i in range(10, 0, -2):
    print(i)
    
