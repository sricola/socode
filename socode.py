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

def sricola():
    print "Welcome to soCode!!"

def lafin(): # Please speak proper french :)
    print "Goodbye Social World!"
    
def JesseAldridge():
    def wrap(f):
      def new_f():
        for i in range(3):
          f()
      return new_f

    g = globals()
    for k, v in g.iteritems():
      if callable(v) and k != 'JesseAldridge':
        g[k] = wrap(v)
    
if __name__ == "__main__":
    JesseAldridge()
    sricola()
    lafin()
