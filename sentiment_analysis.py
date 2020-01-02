"""
Sonya Cao
COMPSCI 1026
BAUER
11/13/19
Sentiment Analysis: program used to analyze Twitter tweets for the Eastern, Central, Mountain and Pacific region
information.
"""
from string import punctuation

# constants for the longitude and latitude boundaries of the regions
MAX_LONG = 49.189787
MIN_LONG = 24.660845
P1_LAT = -67.444574
P3_LAT = -87.518395
P5_LAT = -101.998892
P7_LAT = -115.236428
P9_LAT = -125.242264


def compute_tweets(tweets, keywords):  # function to determine the happiness score, number of keywords, and total tweets for each timezone
   #if the tweet file and/or the keyword file given does not exist, an IOError will be thrown, an empty list returned and an error statment printed
    try:
        t = open(tweets, encoding='utf‐8', errors='ignore')
    except IOError:
        print('Tweets file does not exist')
        t.close()
        return []
    try:
        k = open(keywords, encoding='utf‐8', errors='ignore')
    except IOError:
        print('Keywords file does not exist')
        k.close()
        return []

    keydict = {}  # keydict is a dictionary for all the keywords and the sentiment value associated with each one
    #variables for the total tweets for each region and list of total sentiment values for each tweet in each respective region
    eastern = 0
    central = 0
    mountain = 0
    pacific = 0
    easternlist = []
    centrallist = []
    mountainlist =[]
    pacificlist = []

    line = k.readline()
    while line != "": #will continue to loop until the end of the file is reached
        words = line.split(',') #list made up of the keyword and its sentiment value

        # if the keywords file is not in the expected format, the dictionary for keywords remains empty
        try:
            keydict[words[0]] = int(words[1].strip()) #adding the keyword as a new key and the sentiment value as its respective value into the dictionary
        except ValueError:
            print("keywords file is in wrong format")
            break
        line = k.readline()
    k.close()

    line = t.readline()
    while line != "": #will continue to loop until the end of the file is reached
        score = 0 #variable that stores the happiness score of the tweet
        key = 0 #variable that stores the total number of keywords in the tweet
        senti = 0 #variable that stores the sum of the sentiment value of the keywords mentioned in the tweet

        words = line.split() #creating a list of the words in the tweet

        #stripping the first and second element in the list of "words" in the tweet to determine the longitude and latitude
        #if the tweets file is not in the expected format, returns empty list
        try:
            long = float(words[0].strip(",[]"))
        except ValueError:
            print("tweets file is in wrong format")
            return []

        lat = float(words[1].strip(",[]"))

        for word in words: #looping through each word in the tweet
            word = word.strip(punctuation) #removing all punctuation from the beginning and end of each word in the tweet
            #if the word is in one of the keys in the dictionary, total key and total sentiment are updated
            word = word.lower()
            if word in keydict:
                key += 1
                senti += keydict[word]

        if key > 0:
            score = senti/key

        region = regioncalc(long, lat)  # calling the regioncalc function to determine which region the tweet is from
        # depending on which region the tweet is from, the region tweet total is updated and the score is added to its region list

        if region == "eastern":
            eastern += 1
            easternlist.append(score)
        elif region == "central":
            central += 1
            centrallist.append(score)
        elif region == "mountain":
            mountain += 1
            mountainlist.append(score)
        elif region == "pacific":
            pacific += 1
            pacificlist.append(score)

        line = t.readline()
    t.close()

    #a list of tuples is returned with each tuple representing a region
    return [(scorecalc(easternlist, keycalc(easternlist)), keycalc(easternlist), eastern), (scorecalc(centrallist, keycalc(centrallist)), keycalc(centrallist), central),
            (scorecalc(mountainlist, keycalc(mountainlist)), keycalc(mountainlist), mountain), (scorecalc(pacificlist, keycalc(pacificlist)), keycalc(pacificlist), pacific)]

def scorecalc(regionlist, totalkey): #returns the sum of all the sentiment values of tweets in the region divided by the number of tweets with keywords in the region
    if totalkey > 0:
        totalscore = sum(regionlist)
        return totalscore/totalkey
    else:
        return 0

def keycalc(regionlist): #returns the number of keyword tweets in the region
    totalkey = 0

    for i in regionlist:
        if i > 0:
            totalkey += 1

    return totalkey


def regioncalc(long, lat): #returns the region the tweet is from
    if MIN_LONG <= long <= MAX_LONG: #if the tweet is not within the longitude boundaries, nothing is returned
        #if it is within the longitude boundaries, eastern, central, mountain or nothing will be returned depending on where it falls within the latitude boundaries
        if P1_LAT >= lat >= P3_LAT:
            return "eastern"
        elif P3_LAT >= lat >= P5_LAT:
            return "central"
        elif P5_LAT >= lat >= P7_LAT:
            return "mountain"
        elif P7_LAT >= lat >= P9_LAT:
            return "pacific"
        else:
            return ""
    else:
        return ""

