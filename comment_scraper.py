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

def gather_comments(bot, subreddit_name, num_submissions, num_comments, get_comments):

    posts = []
    post_sentiment = {}
    comments = []
    replies = []

    subreddit = get_subreddit(bot, subreddit_name)

    for post in subreddit.controversial('all', limit=num_submissions):

        #Lets you gather replies to comments
        post.comments.replace_more(limit=1)

        #Get the votes for the post
        post_votes = get_votes(post)

        #Parse the post title
        post_title_blob = TextBlob(clean(post.title))

        #Parse the self-text for the post
        post_self_text_blob = TextBlob(clean(post.selftext))

        #Gather sentiment for title and self-text
        post_sentiment['title'] = post_title_blob.sentiment_assessments
        post_sentiment['self_text'] = post_self_text_blob.sentiment_assessments

        #Append post object to list of posts
        posts.append(Post(post_title_blob, post_self_text_blob, post_sentiment, post_votes))
        
        post_sentiment = {}

        if get_comments:

            for comment in post.comments[:num_comments]:

                #Get the votes for the comment
                comment_votes = get_votes(comment)

                #Parse the comment
                comment_blob = TextBlob(clean(post.title))

                #Gather replies for the comment
                replies = get_replies(comment)
            
                #Append comment object to list of comments 
                comments.append(Comment(comment_blob, replies, comment_blob.sentiment_assessments, comment_votes))

        else:
            comments = []

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

def get_replies(comment):

    replies = []

    for reply in comment.replies:

        reply_sentiment = {}

        reply_votes = get_votes(reply)
        reply_blob = TextBlob(clean(reply.body))

        reply_sentiment['reply'] = reply_blob.sentiment_assessments
        
        replies.append(Reply(reply_blob, reply_sentiment, reply_votes))

    return replies

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
