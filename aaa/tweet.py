import tweepy

consumer_key = 'n31cVsMqaXjvItpCWT41reXxN'
consumer_secret = 'RTrA1IQQrqilxdGBlPxsaZSUSZv7LldHX90miybFJWONNImniV'
access_token = '1463648411115130881-wqMRTV96AwCWJVtpeVnBVAUQDlBpEl'
access_token_secret = 'FkA88GOBNz2yRvYPXJWoy2IJ5LxJ2xF0PI8hebRJr1kHx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status("Hello world")
