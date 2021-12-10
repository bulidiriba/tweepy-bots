import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("lsvCzTohCFFjNXIbHPcgqhQZh", "ECOvhM6Mde2SzNYcnRdRw2tgqwwM2mpR2wRe1fRkfyf3056mEg")
auth.set_access_token("4107572963-JVpQTXOreSNGaBnxiXw88dKu8q6oZTm5sWgOwF9", "AtNLKoXCXOTkrosnj0Nt8zmqLTjg3i4P0iCXREA6GImDy")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Ok")
except:
    print("Error during authentication")

# To get the latest list of tweet from timeline(20 by default)
timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

# To make a tweet
#api.update_status("Test tweet from Tweepy Python")

# to get the details of given user
user = api.get_user(screen_name="MikezGarcia")
print("User details")
print("name: ", user.name)
print("description: ", user.description)
print("location: ", user.location)

print("Last 20 followers of the user: ")
for follower in user.followers():
    print(follower.name)


# To follow or create a freindship(e.g to follow @realpython)
api.create_friendship("realpython")
