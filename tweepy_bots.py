import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("[API_KEY]", "[API_KEY_SECRET]")
auth.set_access_token("[Access_Token]", "[Access_Token_Secret]")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Ok")
except:
    print("Error during authentication")

