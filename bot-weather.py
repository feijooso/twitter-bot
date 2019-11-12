import tweepy
import time
import requests

from secrets import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api_address='http://api.openweathermap.org/data/2.5/weather?appid=902f718fe489465ff24fc7dc39cabc82&q=Buenos%20Aires'

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if 'humedad' in mention.full_text.lower():
        	texto = "La humedad en Buenos Aires es de " + main[humidity] +"%"
        elif 'maxima' in mention.full_text.lower() or 'minima' in mention.full_text.lower():
        	texto = "La maxima es de " +main[temp_min]+ "y la minima de "+main[temp_max]
        else: 
        	texto=" La temperatura en Buenos Aires es de "+str(temperature)+" grados y con "+ description

        api.update_status('@'+ mention.user.screen_name + texto, mention.id)
        # if 'hola' in mention.full_text.lower():
        #     print('found hola!', flush=True)
        #     print('responding back...', flush=True)
        #     api.update_status('@' + mention.user.screen_name +
        #             ' hola back to you!', mention.id)

while True:
	json_data = requests.get(api_address).json()
	main = json_data['main']
	weather = json_data['weather']
	temperature = int(main['temp']) - 273
	description = weather[0]['description']
	reply_to_tweets()
	time.sleep(15)