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


def get_titles_and_comments(subreddit='stocks', limit=6, num_comments=3, skip_first=2):   # skip_first are pinned comments
    subreddit = reddit.subreddit(subreddit)
    title_and_comments = {}

    for counter,post in enumerate(subreddit.hot(limit=limit)):

        if counter < skip_first:
            continue
        counter += (1-skip_first)

        title_and_comments[counter] = ""
        # PRAW Documentation
        submission = reddit.submission(post.id)
        title = post.title

        title_and_comments[counter] += "Title: " + title + "\n\n"
        title_and_comments[counter] += "Comments: \n\n"

        comment_counter = 0
        for comment in submission.comments:
            if not comment.body == "[deleted]":
                title_and_comments[counter] += comment.body + "\n"
                comment_counter += 1
            if comment_counter == num_comments:
                break
    return title_and_comments


titles_and_comments = get_titles_and_comments()
print(titles_and_comments)


def create_prompt(title_and_comments):
    task = "Return the stock ticker or company name mentioned in the following comments and classify the sentiment " \
           "around the company as positive, negative, or neutral. If no ticker or company is mentioned write 'No company" \
           "mentioned' \n\n "
