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
import getpass
import re
    
def doctorpangloss():
    raw = requests.get('https://raw.github.com/sricola/socode/master/socode.py').content
    matches = re.sub(r'doctorpangloss\(\)\n', r'doctorpangloss()\ndoctorpangloss()\n', raw, re.M|re.I|re.G)
    print raw

def binary132():
    print "Perl is better.  PS everyone is lazy"

def sricola():
    print "Welcome to soCode!!"

def bencooling():
  print "I don't know Python; I don't belong here"
    
def kisom():
    def zgohr(city): # JesseAldridge breaks top level funcs with parms
        weather = json.loads(requests.
                             get('http://api.openweathermap.org'
                                 '/data/2.1/find/name?q=%s' % city).content)
        kelvin = weather['list'][0]['main']['temp']
        fahrenheit = 9/5*(kelvin - 273) + 32
        print 'and it is too damn cold' \
            if fahrenheit < 50 else 'and the temperature outside is tolerable'

    ip = requests.get('http://ifconfig.me/ip').content
    geoip = json.loads(requests.get('http://freegeoip.net/json/').content)
    print 'there once was a coder from', geoip['country_name']
    zgohr(geoip['city'])
    
def evinugur():
    print 'there is a ', (random.random()*100), "% chance that something cool will come from this..."
    
def lafin(): # Please speak proper french :)
    print "Goodbye Social World!"
    print "\nStarted with <3 in Brooklyn, NY\n"

def prezjordan():
    h,s='.;*&8#',''
    for q in range(801):
        if q%40==0:print s;s=''
        i,k=0,0
        while(abs(k)<2*(i<15)):k,i=k**2+complex(q%40*.075-2,q/40*-.1+1),i+1
        s+=h[i/3]*2
    
def JesseAldridge():
    def wrap(f):
      def new_f():
        for i in range(1):
          f()
      return new_f

    g = globals()
    for k, v in g.iteritems():
      if callable(v) and k != 'JesseAldridge':
        g[k] = wrap(v)
    
def shuhaowu(): # Call me last! :D
    l = locals()
    for f in l.keys():
        if not (f.startswith("_") or f == "shuhaowu"):
            del l[f] # ^_^

    print "Goodbye, cruel world"
    
def agoebel():
    print "America!"

def tcr():
    print "You know we love you, ", getpass.getuser(), "."

def fmazon3():
    print "%d" % 0xDEADC0DE
    
if __name__ == "__main__":
    evinugur()
    JesseAldridge()
    sricola()
    kisom()
    prezjordan()
    tcr()
    agoebel()
    binary132()
    doctorpangloss()
    lafin()
    fmazon3()
