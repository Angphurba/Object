print "Time to play hangman!"

import random
WORDS = ("jump", "run", "dive", "care", "smoke", "pipe", "left", "right", "hand", "finger", "bone", "pink", "peach")
word = random.choice(WORDS)
guesses = ''
turns = 6

while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:    
            print char,    
        else:
            print "*",     
            failed += 1    
    if failed == 0:        
        print "You win!"  
        break              

    print
    guess = raw_input("Guess the word:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print "Wrong"    
        print "You have", + turns, 'more guesses' 
        if turns == 5:
            print "-------"
            print "   |   "
            print "   0   "
        if turns == 4:
            print "-------"
            print "   |   "
            print "   0   "
            print "   | \ "
        if turns == 3: 
            print "-------"
            print "   |   "
            print "   0   "
            print " / | \ "
        if turns == 2:
            print "-------"
            print "   |   "
            print "   0   "
            print " / | \ "
            print "   |   "
        if turns == 1:      
            print "-------"
            print "   |   "
            print "   0   "
            print " / | \ "
            print "   |   "
            print " /   \ "
        if turns == 0:
            print "-------"
            print "   |   "
            print "   0   "
            print " / | \ "
            print "   |   "
            print " /   \ "
            print "/     \ "
            print "You lose! The word is; "
            print(word)