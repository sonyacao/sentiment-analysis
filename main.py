from sentiment_analysis import compute_tweets

tweets = input("Please enter the name of the tweets file")
keywords = input("Please enter the name of the keywords file")
results = compute_tweets(tweets, keywords) #calling the compute function to find the results for each region

#printing out the results in a readable form
if results != []:
    print("EASTERN:","\nHappiness Score: ", results[0][0], "\nNumber of Tweets in Timezone: ", results[0][1], "\nTotal Number of Tweets in Timezone: ", results[0][2],"\n")
    print("CENTRAL:", "\nHappiness Score: ", results[1][0], "\nNumber of Tweets in Timezone: ", results[1][1], "\nTotal Number of Tweets in Timezone: ", results[1][2],"\n")
    print("MOUNTAIN:", "\nHappiness Score: ", results[2][0], "\nNumber of Tweets in Timezone: ", results[2][1], "\nTotal Number of Tweets in Timezone: ", results[2][2],"\n")
    print("PACIFIC:", "\nHappiness Score: ", results[3][0], "\nNumber of Tweets in Timezone: ", results[3][1], "\nTotal Number of Tweets in Timezone: ", results[3][2])
else:
    print("EASTERN:","\nHappiness Score: 0", "\nNumber of Tweets in Timezone: 0", "\nTotal Number of Tweets in Timezone: 0", "\n")
    print("CENTRAL:", "\nHappiness Score: 0", "\nNumber of Tweets in Timezone: 0", "\nTotal Number of Tweets in Timezone: 0","\n")
    print("MOUNTAIN:", "\nHappiness Score: 0", "\nNumber of Tweets in Timezone: 0", "\nTotal Number of Tweets in Timezone: 0", "\n")
    print("PACIFIC:", "\nHappiness Score: 0", "\nNumber of Tweets in Timezone: 0", "\nTotal Number of Tweets in Timezone: 0")
