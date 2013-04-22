#!/usr/bin/env python

# Welcome to soCode, the social coding experiment.
# Here are the rules!
#       - Add a function with your github name as its name.
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
import hashlib
import os

def heinzf():
    """Compare itself with the raw code github. If there's something new, it updates the file localy."""
    git_file = requests.get('https://raw.github.com/sricola/socode/master/socode.py').content
    git_hash = hashlib.sha256(git_file).hexdigest()
    with open(os.path.realpath(__file__),'r+') as f:
        local_file = f.read()
    f.close()
    local_hash = hashlib.sha256(local_file).hexdigest()

    if  local_hash != git_hash:
        with open(os.path.realpath(__file__),'w+') as f:
            f.write(git_file)
            print 'I update myself, when I think about you, lalalala'
        f.close()

def doctorpangloss():
    raw = requests.get('https://raw.github.com/sricola/socode/master/socode.py').content
    # not sure what is being achieved here - @sricola
    #matches = re.sub(r'doctorpangloss\(\)\n', r'doctorpangloss()\ndoctorpangloss()\n', raw, re.M|re.I|re.G)
    #print raw

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

def daniel_dressler(): # really daniel-dressler
    return 42

def evinugur():
    print 'there is a ', (random.random()*100), "% chance that something cool will come from this..."

def ncammarata():
    tweets = json.loads(requests.get("https://search.twitter.com/search.json?q=a").content)
    tweet = tweets['results'][0]['text']
    print "Random Tweet:", tweet

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
      def new_f(*args, **kwargs):
        # changing this back to one, it really slows things down with the requests - @sricola
        f(*args, **kwargs)
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

def peterwallhead():
    print '\n'.join('Fizz'*(not i%3) + 'Buzz'*(not i%5) or str(i) for i in range(1, 101))

def cyclo():
    print "!dnalgnE morf olleH"[::-1]

def chrisgw():
    print "meh"

def jpadilla():
    repo = requests.get('https://api.github.com/repos/sricola/socode').json()
    print 'Forked {} times'.format(repo['forks_count'])


if __name__ == "__main__":
    jpadilla()
    heinzf()
    evinugur()
    JesseAldridge()
    sricola()
    kisom()
    ncammarata()
    prezjordan()
    tcr()
    agoebel()
    cyclo()
    binary132()
    doctorpangloss()
    chrisgw()
    fmazon3()

    # special
    lafin()
