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

subreddit_stocks = reddit.subreddit("stock")

# access the first 5 hot posts
for post in subreddit_stocks.hot(limit=5):   # Grabs info from "stock" title limited to 5
    print(post.title)
    submission = reddit.submission(post.id)
    # print top 2 comments per tittle submission
    counter = 0
    for comment in submission.comments:
        print(comment.body)   # text of comment
        # skips over deleted comments
        if comment.body == ["deleted"]:
            pass
        # Let's say we don't want to surpass more than 2 comments per title
        counter += 1
        if counter == 2:
            break


# 3 most uploaded comments in those hot posts
