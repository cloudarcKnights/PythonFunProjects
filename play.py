def count(x):
    guess = 0 
    while guess < x:
        guess = (input(f'Can you count all the way to {x}'))
        if guess == ('yes'):
            print('Start counting')

count('100')
