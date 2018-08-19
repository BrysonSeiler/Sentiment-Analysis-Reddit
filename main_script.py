import config
import praw

import comment_scraper as cs
import statistics as stat

from pprint import pprint


def main():

    bot = login()

    subreddit_name = str(input("Input a subreddit that you would like to analyze: "))

    num_submissions = 1
    num_comments = 1
    reply_depth = 1

    posts, comments = cs.gather_comments(bot, subreddit_name, num_submissions, num_comments)

    stat.analyze_post_sentiment(posts)
    stat.analyze_comment_sentiment(comments)

    


def login():

    bot = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "Sentiment_Analysis")

    return bot

if __name__ == '__main__':
    main()