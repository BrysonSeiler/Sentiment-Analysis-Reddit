import re
from textblob import TextBlob

from praw.models import MoreComments
from pprint import pprint

#python -m textblob.download_corpora


class Comment: 

    def __init__(self, body, replies, sentiment, votes):
        self.body = body
        self.replies = replies
        self.sentiment = sentiment
        self.votes = votes

class Reply:
    def __init__(self, body, sentiment, votes):
        self.body = body
        self.sentiment = sentiment
        self.votes = votes

class Post:

    def __init__(self, title, self_text, sentiment, votes):
        self.title = title
        self.self_text = self_text
        self.sentiment = sentiment
        self.votes = votes

def gather_comments(bot, subreddit_name, num_submissions, num_comments):

    posts = []
    post_sentiment = {}
    comments = []
    replies = []

    subreddit = get_subreddit(bot, subreddit_name)

    for post in subreddit.controversial('all', limit=num_submissions):

        post_votes = get_votes(post)

        #print(post.title)
        post_title_blob = TextBlob(clean(post.title))
        post_self_text_blob = TextBlob(clean(post.selftext))

        #pprint(post_self_text_blob)

        post_sentiment['title'] = post_title_blob.sentiment_assessments
        post_sentiment['self_text'] = post_self_text_blob.sentiment_assessments

        posts.append(Post(post_title_blob, post_self_text_blob, post_sentiment, post_votes))

        for comment in post.comments[:num_comments]:

            if isinstance(comment, MoreComments):
                continue

            comment_votes = get_votes(comment)

            comment_blob = TextBlob(clean(comment.body))

            for reply in comment.replies:

                reply_blob = TextBlob(clean(reply.body))
                reply_votes = get_votes(reply)

                replies.append(Reply(clean(reply.body), reply_blob, reply_votes))

            comments.append(Comment(comment_blob, comment.replies, comment_blob.sentiment_assessments, comment_votes))

    return posts, comments

def get_subreddit(bot, subreddit_name):
    subreddit_obj = bot.subreddit(subreddit_name)
    return subreddit_obj

def get_votes(text):

    vote = {}

    vote['up'] = text.ups
    vote['down'] = text.downs
    vote['score'] = text.score

    return vote

def clean(post):

    #Remove parentheses
    re_p = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", post)

    #Remove links
    re_l = re.sub(r"http\S+|([\(\[]).*?([\)\]])", "", re_p)

    #Remove special characters
    re_s = re.sub(r"[^A-Za-z \—]+", " ", re_l)

    #Remove capitalization
    re_c = re.sub('[A-Z]+', lambda m: m.group(0).lower(), re_s)

    #Remove excess white space
    filtered_post = " ".join(re_c.split())

    return filtered_post
