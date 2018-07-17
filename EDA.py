import json
from collections import Counter, defaultdict
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


#########################################################################
# this script allows for basic EDA of the reviews contained in the
# Yelp data. 
#########################################################################

def load_data():
    """loads the multi-line JSON file for initial analysis"""
    data = []   
    with open('../dataset/review.json', 'r') as f:
        for line in f:
            data.append(json.loads(line))
    return data

def sort_data():
    """puts the data into a DataFrame for fast and easy analysis"""
    data = load_data()  #load everything
    num_reviews = 4736897   #i found this separately
    #for now, let's just get the necessary fields for the 1 and 5 star reviews
    data_dict = {'business_id' : [None] * num_reviews,
                 #'cool' : np.zeros(num_reviews, dtype = np.uint16),
                 #'date' : [None] * num_reviews,
                 #'funny' : np.zeros(num_reviews, dtype = np.uint16),
                 #'review_id' : [None] * num_reviews,
                 'stars' : np.zeros(num_reviews, dtype = np.uint8),
                 'text' : [None] * num_reviews,
                 #'useful' : np.zeros(num_reviews, dtype = np.uint16),
                 'user_id' : [None] * num_reviews}
    #put into a dict for easy conversion to DataFrame
    for i, review in enumerate(data):
        print(i, end = ' ')
        #here we should do minimal processing of the text first
        #strip and replace \n with a space
        if review['stars'] == 1 or review['stars'] == 5:
            review['text'] = review['text'].strip().replace('\n', ' ')
            data_dict['business_id'][i] = review['business_id']
            data_dict['stars'][i] = review['stars']
            data_dict['text'][i] = review['text']
            data_dict['user_id'][i] = review['user_id']
    df = pd.DataFrame(data_dict)
    return df

def stars_plot():
    """create a simple pie chart showing the distribution of the numbers of
    stars given amongst the reviews, probably can use in the paper"""
    data = load_data()
    num_reviews = 4736897
    stars = np.zeros(num_reviews, dtype = np.uint8)
    labels = [str(x) + ' stars' for x in range(1,6)]
    for i, review in enumerate(data):
        stars[i] = review['stars']
    plt.pie(stars)
    plt.axis('equal')
    plt.show()
