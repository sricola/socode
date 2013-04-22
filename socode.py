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

def kghose():
    import curses, time
    
    def main_loop(window):
        window.clear()
        N = 100
        primes = []
        this_prime = 2
        keep_finding = True
        numbers = [n for n in xrange(N+1)]
        numbers[1] = None
        while keep_finding:
            primes.append(this_prime)
            for n in xrange(2*this_prime, N+1, this_prime):
                numbers[n] = None
                paint_grid(window, numbers)
          
            keep_finding = False
            for n in xrange(this_prime+1, N+1):
                if numbers[n] is not None:
                    this_prime = n
                    keep_finding = True
                    break
    
    
    def paint_grid(window, numbers):
        for row in xrange(10):
            for col in xrange(10):
              n = 10*row + col + 1
              if numbers[n] is not None:
                  s = str(n)
              else:
                  s = '   '
              window.addstr(row, 3*col, s)
        window.refresh()
        time.sleep(.1)
    
    curses.wrapper(main_loop)
    

def lefin():
    print "Goodbye Social World!"
    
if __name__ == "__main__":
    sricola()
    lefin()
