import random, time

choice = ['rock', 'paper', 'scissors']

def play():
    while True:
        comp = random.choice(choice)
        time.sleep(0.5)
        guess = input('rock, paper or scissors? ')
        
        if comp == 'rock' and guess == 'scissors' or comp == 'scissors' and guess == 'paper' or comp == 'paper' and guess == 'rock':
            print('Comp wins by', comp)
            break
        if guess == 'rock' and comp == 'scissors' or guess == 'scissors' and comp == 'paper' or guess == 'paper' and comp == 'rock':
            print('You win by', guess)
            print('Comp guess was', comp)
            break
        if guess == comp:
            print('Tie! Both have', comp)
            break
    return guess

play()
again = input('Wanna play again?(y/n) ').lower()
if again == 'y':
    play()
elif again == 'n':
    print('Thanks for playing!')
else:
    print('Not a valid option.')