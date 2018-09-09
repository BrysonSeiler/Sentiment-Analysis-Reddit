from pprint import pprint

import seaborn as sns
sns.set()
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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


    self_text_df = pd.DataFrame(
        {'Polarity': self_text_polarity,
         'Subjectivity': self_text_subjectivity
        })

    #print(self_text_polarity)
    #print(self_text_subjectivity)
    plt.hist(self_text_polarity, bins=30, alpha=0.5)
    plt.hist(self_text_subjectivity, bins=30, alpha=0.5)

    for key in self_text_df.keys():
        ax=sns.kdeplot(self_text_df[key], shade=True)

    ax.set_title("Self Text")
    plt.show()


#def analyze_comment_sentiment(comments):







