from pprint import pprint

def analyze_post_sentiment(posts):

    title_polarity = []
    title_subjectivity = []

    self_text_polarity = []
    self_text_subjectivity = []


    for i in range(len(posts)):

        title_polarity.append(posts[i].sentiment['title'].polarity)
        title_subjectivity.append(posts[i].sentiment['title'].subjectivity)

        self_text_polarity.append(posts[i].sentiment['self_text'].polarity)
        self_text_subjectivity.append(posts[i].sentiment['self_text'].subjectivity)


#def analyze_comment_sentiment(comments):

    
#    polarity = []
#    subjectivity = []

    #for i in range(len(comments)):

        #pprint(comments[i].replies)

        #for reply in comments[i].replies:






