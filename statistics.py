from pprint import pprint

def analyze_post_sentiment(posts):

    polarity = []
    subjectivity = []

    for i in range(len(posts)):

        polarity.append(posts[i].sentiment['title'].polarity)
        subjectivity.append(posts[i].sentiment['title'].subjectivity)




def analyze_comment_sentiment(comments):

    
    polarity = []
    subjectivity = []

    for i in range(len(comments)):

        pprint(comments[i].replies)

        for reply in comments[i].replies:
            print(reply.body)


    print(polarity)



