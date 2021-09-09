from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import tweepy
import pandas as pd


# twitter attmept
consumer_key = 'Yv1pCAmxAYQGRnU7PJLKM3C0u'
consumer_secret ='NZYNFJMsaMgRuzA3WO5u0GrAVSOKbXmV5dfdo70vFXHUQj8TTD'
access_token = '3100791571-KLx1qs8DlxT20HdF5ym65lkKTdwYgSrPH1h9GUr'
access_secret = '7ge6iFUPFuwAtFwzGssMkpzApsFEapyZPEgVFyQmoPxN7'


def home(request):
    return render(request,'home.html')

def getTweetsByHashtag(request):
    #try:
        if request.method =='POST':
            Tweetcount= request.POST['tweetcount']
            Hashtagname= request.POST['Hashtagname']
            
            newhashtag=""

            if Tweetcount == "":
                Tweetcount=30 
            
            if Hashtagname[0]!='#':
                newhashtag = Hashtagname[:0] + '#' + Hashtagname[0:]
            else:
                newhashtag = Hashtagname

            print(Tweetcount,newhashtag)
            
            TweetList=fullTweet(int(Tweetcount),newhashtag)
            #tweetsProcessing()
            return render(request, 'tweetsReturn.html', {'TweetList':TweetList})

        else:
            messages.error(request,'Data has invalid')
            return render(request,'home.html')
    #


def getTweetsByUserId(request):
    #try:
        if request.method =='POST':
            Tweetcount= request.POST['tweetcount']
            Username= request.POST['Username']
            
            if Tweetcount == "":
                Tweetcount=30 
            
            TweetList=fullTweet_User(int(Tweetcount),Username)
            #tweetsProcessing()
            return render(request, 'UserTweet.html', {'TweetList':TweetList})

        else:
            messages.error(request,'Data has invalid')
            return render(request,'home.html')


def fullTweet(max_tweet,text_query):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    
    # Creation of query method using parameters
    tweets = tweepy.Cursor(api.search,q=text_query).items(max_tweet)
    
    # Pulling information from tweets iterable object
    # Add or remove tweet information you want in the below list comprehension

    tweets_list = [[tweet.user.name, tweet.user.screen_name,tweet.source,
                    tweet.user.id_str,tweet.created_at, tweet.text, tweet.retweet_count,
                    tweet.favorite_count] for tweet in tweets]
    return tweets_list

    # Creation of dataframe from tweets_list
    # Did not include column names to simplify code 
    tweets_df = pd.DataFrame(tweets_list)
    print(tweets_df)

def fullTweet_User(max_tweet,username):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    
    # Creation of query method using parameters
    tweets = tweepy.Cursor(api.user_timeline,id=username ).items(max_tweet)
    
    # Pulling information from tweets iterable object
    # Add or remove tweet information you want in the below list comprehension

    tweets_list = [[tweet.user.name, tweet.user.screen_name,tweet.source,
                    tweet.user.id_str,tweet.created_at, tweet.text, tweet.retweet_count,
                    tweet.favorite_count,tweet.user.url,tweet.user.description, tweet.user.followers_count
                    ] for tweet in tweets]
    return tweets_list