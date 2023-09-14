import os
import praw
import openai

client_id = os.getenv('CLIENT_ID')
reddit_secret = os.getenv('REDDIT_SECRET')

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=reddit_secret,
    user_agent="Sentiment analysis test"
)

# Connect to redit and grab information from "stock" title limited to 5
for submission in reddit.subreddit("stock").hot(limit=5):
    print(submission.title)
