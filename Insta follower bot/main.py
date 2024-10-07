
from Insta_follower import InstaFollower

SIMILAR_ACCOUNT = "Insta acc"  # Change this to an account of your choice
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"

bot = InstaFollower()
bot.login(USERNAME, PASSWORD)
bot.find_followers(SIMILAR_ACCOUNT)
bot.follow()