import tweepy
import time
import requests

from secrets import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_tweet.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = f_read.read().strip()
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def tweet():
    print('reading dms...', flush=True)
    last_tweet = retrieve_last_seen_id(FILE_NAME)
    dms = api.list_direct_messages(1)
    if (len(dms)>0):
        text = dms[0].message_create['message_data']['text']
        if(last_tweet != text):
            for dm in range(0,len(dms)):
                print("---------")
                print(text)
        else:
            print('de')

while True:
	tweet()
	time.sleep(5)