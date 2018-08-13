import config
import praw



def main():

    bot = login()






def login():

    bot = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "Sentiment_Analysis")

    return bot

if __name__ == '__main__':
    main()