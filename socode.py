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

import json
import requests
import random
def sricola():
    print "Welcome to soCode!!"
    
def kisom():
    ip = requests.get('http://ifconfig.me/ip').content
    geoip = json.loads(requests.get('http://freegeoip.net/json/' + ip).content)['country']
    print 'there once was a coder from', geoip
    
def evinugur():
    print 'there is a ', (random.random()*100), "% change that something cool will come from this..."
    
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
    evinugur()
    JesseAldridge()
    sricola()
    kisom()
    lafin()
