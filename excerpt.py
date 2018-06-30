import os, subprocess
import random
#From gpiozero import button

#button = Button(2)

def printBookExcerpt():   
    excerpt = random.choice(os.listdir(path='excerpts'))
    excerpt = 'excerpts/' + excerpt
    subprocess.run(["lp", excerpt])

#button.waitforpress()
#button.when_pressed = printBookExcerpt() 

printBookExcerpt()
