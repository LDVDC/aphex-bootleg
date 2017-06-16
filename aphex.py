import random
import time
import curses

words = open('words').read().splitlines()
width = 50
lines = 5
speed = 0.05
dottiness = 1000
chars = '///\:*{}()[]+-_'

def change_word(wordlist,corr,charlist):
    word_str = ''
    word = random.choice(wordlist).title()
    for i in word:
        if random.random() * 20 < corr:
            word_str += random.choice(charlist)
        else:
            word_str += i
    return word_str

def change_trail(charlist, width, dots, corr, word):
    charlist_full = charlist * corr + '.' * dots
    endstr = ''
    for i in range(width - len(word)):
        endstr += random.choice(charlist_full)
    return endstr

def full_trail(charlist, width, dots, corr, word, lines):
    endstr = ''
    endstr += change_trail(charlist,width,dots,corr,word)
    for i in range(lines - 1):
        endstr += '\n'
        endstr += change_trail(charlist,width,dots,corr,'')
    return endstr
    
def main(stdscr):
    # Don't wait for user input on getch()
    stdscr.nodelay(1)
    
    corrupt_chance = 0
    # Generate initial word and trail
    word = change_word(words,corrupt_chance,chars)
    trail = full_trail(chars,width,dottiness,corrupt_chance,word,lines)
    
    while True:
        # Clear the screen
        stdscr.clear()
        
        # Quit if q is pressed
        if stdscr.getch() == ord('q'):
            break
        else:
            pass
        if random.random() < 0.02:
            corrupt_chance += 20
        elif random.random() < 0.08:
            corrupt_chance += 1 

        if random.random() < 0.6:
            word = change_word(words,corrupt_chance,chars)
        
        trail = full_trail(chars,width,dottiness,corrupt_chance,word,lines)

        if corrupt_chance > 20:
            corrupt_chance -= 3
        elif corrupt_chance > 0:
            corrupt_chance -= 1

        stdscr.addstr(0,0, word + trail)
        stdscr.refresh()

        time.sleep(speed + (random.random() * speed - (speed/2)))
        
curses.wrapper(main)
