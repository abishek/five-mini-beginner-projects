from random import randint

MIN_RAND = 1
MAX_RAND = 1000

def guess_the_number() :
    
    number_to_guess = randint(MIN_RAND, MAX_RAND)
    user_guess = MIN_RAND

    while user_guess :
        try :
            user_guess = int(raw_input('Enter a number you guess : '))
            if user_guess == number_to_guess :
                print "Great! You found the number I generated."
                return

            elif user_guess > number_to_guess :
                if (user_guess - number_to_guess) > 100 :
                    print "Your guess is very high from my generated number."
                else :
                    print "You are quite close, just a little high. Try again!"

            else :
                if (number_to_guess - user_guess) > 100 :
                    print "Your guess is too low from my generated number."
                else :
                    print "You are quite close, just a little low. Try again!"
        except ValueError, e :
            print "I give up! You should enter a number."


if __name__ == '__main__' :

    guess_the_number()

