import tweepy
print('hello, im bot!')

from secrets import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

for mention in mentions:
	print(str(mention.id) + ' ' + mention.text)
