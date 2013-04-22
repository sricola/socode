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
import string
import math
import sys    
import inspect

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

def adelevie():
    pass

def piperchester():
    print "I love this idea. Hailing from Rochester, NY!"

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

# Generate a random nonsense word with a vowel:consolant ratio of 1:5
def taylorlapeyre():
    word = []
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels     = "aeiou"

    for i in range(random.randint(3, 15)):
        if i % 5 == 0:
            letter = random.choice(vowels)
        else:
            letter = random.choice(consonants)
        word.append(letter)

    return ''.join(word)


def lafin(): # Please speak proper french :)
    print "Goodbye Social World!"
    print "\nStarted with <3 in Brooklyn, NY\n"

def prezjordan():
    h,s='.;*&8#',''
    for q in range(HoLyVieR(43, 1013)):
        if q%40==0:print s;s=''
        i,k=0,0
        while(abs(k)<2*(i<15)):k,i=k**2+complex(q%40*.075-2,q/40*-.1+1),i+1
        s+=h[i/3]*2

def JesseAldridge():
    def wrap(f):
      def new_f(*args, **kwargs):
        # changing this back to one, it really slows things down with the requests - @sricola
        return f(*args, **kwargs)
      return new_f

    g = globals()
    for k, v in g.iteritems():
      if callable(v) and k != 'JesseAldridge':
        g[k] = wrap(v)

def eternalmatt():
    print "Never gonna give you up."
    print "Never gonna let you down."
    print "Never gonna run around."
    print "And hurt you."
    
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

def maxmackie(crypt_me):
    """Just try and crack this cipher."""
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    crypt = "mplnkoijbqazdsxcwerfgvhutyQASXZWDVFCERGTBHNYKMJLUPIO4567382901"
    print crypt_me.translate(string.maketrans(abc, crypt))

def uiri():
    with open(os.path.realpath(__file__),'r') as f:
        for line in f.readlines():
            if line.strip()[:5] == "print":
                print line.strip()

def jpadilla():
    repo = requests.get('https://api.github.com/repos/sricola/socode').json()
    try:
        print 'Forked {} times'.format(repo['forks_count'])
    except ValueError:
        pass

def rburgosnavas(name):
    print '-' * (len(name) + 6)
    print "|  " + ' ' * (len(name)) + "  |"
    print "|  " + name + "  |"
    print "|  " + ' ' * (len(name)) + "  |"
    print '-' * (len(name) + 6)

def GeneralZero():# Spin the wheel
    random.choice([obj for name, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isfunction(obj)])()

def bprater():

	print "social coding, the end is near."

def satshabad():
    # this doesn't seem to space right... 
    for x in range(10000):
        r = random.randint(0,1)
        if r == 0:
            print '/'
        else:
            print '\\'

def henghonglee():
    print "#!brain"

def jhgaylor():
    print "Signing in from Starkville, Mississippi."

def mmay():
    url = "http://placekitten.com/%d/%d" %(random.randint(500, 1000), random.randint(500, 1000))
    print "Get your daily dose of kitten at: " + url

def jeffjose():
    print "Hi from India!"

def julio():
    print 111111111 * 111111111;

def ondrae(): # Random compliment. If anyone has a better source, add it in.
    response = requests.get("http://peoplearenice.blogspot.com/p/compliment-list.html")
    lines = response.text.split('\n')
    pattern = '\d+\.\s+(.*)</span>'
    compliments = []
    for line in lines:
        m = re.search(pattern, line)
        if m:
            compliments.append(m.group(1))
    print getpass.getuser() +', ' + compliments[random.randint(1,len(compliments))].lower()

def djrausch():
    print "DAE #HOLO? #NEXUS #HOLOYOLO"

# Compute the modular multiplicative inverse using the extended Euclide algorithm
# See this for more information : http://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Extended_Euclidean_algorithm 
#
# @param nb  Number to be inversed
# @param mod Modular base
# @return The modular multiplicative inverse if found and None if not found.
def HoLyVieR(nb, mod):
    # 1 is a special case, the inverse modulo is always 1 for all modular base #
    if (nb == 1):
        return 1
    
    # We apply the Euclide method to find the GCD step for gcd(nb, mod) #
    stack = []
    a = mod;
    b = nb;
    n = mod / nb;
    r = mod % nb;
    
    while r != 0:
        stack.append([a, b, n, r]);
        
        a = b;
        b = r;
        n = a / b;
        r = a % b;
    
    # If we reach this condition it means there was no step and therefore gcd(nb, mod) != 1 and there is no modular multiplicative inverse #
    if len(stack) == 0:
        return None
    
    values = stack.pop()
    
    # If the last value isn't 1 then gcd(nb, mod) != 1 and there is no modular multiplicative inverse #
    if values[3] != 1:
        return None
    
    # We do the GCD step backward to find the solution #
    f1 = values[3]
    f2 = values[2]
    atN2 = True
    
    while len(stack) > 0:
        values = stack.pop()
        
        if atN2:
            f1 += f2 * values[2]
        else:
            f2 += f1 * values[2]
        
        atN2 = not atN2
    
    f = -f2 if atN2 else f1
    
    # While "f" is a correct result, it's sometimes a negative value and it's usually more 
    # convenient to have a positive value that's in the range of 0 to "mod".
    if (f < 0):
        f += mod * (math.fabs(math.floor(f / mod)) + 1)
    
    return int(f % mod)

def chewxy():
    # because there is nothing better to do after the world has ended.
    pass

def hazirguo():
    print "Mourning for the dead in Sichuan earthquake!\n"
 
def sfrnld():
    print "From Indonesia with love!"

def chris911():
    contributors = requests.get('https://api.github.com/repos/sricola/socode/contributors').json()
    contributors_list = []
    for x in contributors:
        contributors_list.append(x['login'])
    print 'Contributors: '
	print ', '.join(contributors_list) 

def PiersonBro():
    print "My bane was not capability it was randomness."
 
if __name__ == "__main__":
    heinzf() # this thing makes it hard to make sure stuff works, doesn't it?
    uiri() # Can I go first unless you're going to modify the file?
    jpadilla()
    mmay()
    evinugur()
    JesseAldridge()
    sricola()
    kisom()
    ncammarata()
    julio()
    prezjordan()
    tcr()
    jhgaylor()
    henghonglee()
    taylorlapeyre()
    djrausch()
    jeffjose()
    agoebel()
    cyclo()
    binary132()
<<<<<<< HEAD
    sfrnld()
    doctorpangloss()
    chrisgw()
    fmazon3()
    bprater()
    eternalmatt()
    prezjordan()
    shuhaowu()
    chewxy()
    rburgosnavas('CTHULHU LIVES!')
    satshabad()
    ondrae()
    hazirguo()
    chris911()

    # as per instructed, please leave this as the final function
=======
    PiersonBro()
>>>>>>> 0c7762f2a43b5300d07d2bf5d1702a468daffb2b
    lafin()
