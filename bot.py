import tweepy
print('hello, im bot!')

from secrets import * #takes the keys from the secrets.py file
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


mentions = api.mentions_timeline(
                        # last_seen_id,
                        tweet_mode='extended')

for mention in mentions:
	#print(str(mention.id) + ' ' + mention.text)
	if 'hola' in mention.full_text.lower():
		api.update_status('@' + mention.user.screen_name + '#HelloWorld back to you!', mention.id)


