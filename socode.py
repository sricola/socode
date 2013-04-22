#!/usr/bin/env python

# Welcome to soCode, the social coding experiment.
# Here are the rules! 
#       - Add a funtion with your github name as its name.
#       - Your function can do anything and everything, as long as it
#         finishes in a reasonable amount of time (no infinite loops please)
#       - Once your function is written, you can call it from anywhere else in the 
#         already existing exectution chain.
#       - Never entirely delete anyone else's function, edit it if needed.
#       - lefin() should be the last executing function, always

# Lets see if we can make something meaningful out of this.

import datetime

def sricola():
    print "Welcome to soCode!!"
    
def quaz3l():
    print "Today is " + str(datetime.date.today()) + ", quaz3l was here on 2013-04-21"
    if(str(datetime.date.today()) == '2013-04-21'): 
        print "Hey! thats today!"

def lefin():
    print "Goodbye Social World!"
    
if __name__ == "__main__":
    sricola()
    quaz3l()
    lefin()
