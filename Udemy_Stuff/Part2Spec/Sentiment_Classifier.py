#Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. 
#You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. 
#At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

import csv
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
positive_words = []
negative_words = []
fields = ['Number of Retweets','Number of Replies','Positive Score','Negative Score','Net Score']
result_list = []

"""
Allow user to read from textfile and populate a list
"""
def read_text_file(file_name, list):
    with open(file_name , 'r') as in_file:
        for col in in_file:
            if col[0] != ";" and col[0] != '\n':
                list.append(col.strip())

def strip_punctuation(x):
    new_string = ""
    for c in x:
        if c not in punctuation_chars:
            new_string += c.lower()
    return new_string

if __name__=="__main__":
    read_text_file('positive_words.txt' , positive_words)
    read_text_file('negative_words.txt' , negative_words)


    
    with open('project_twitter_data.csv' , 'r') as output_file:
        csv_reader = csv.reader(output_file, delimiter=',')
        for row in csv_reader:
            row_list = []
            positive_count = 0
            negative_count = 0
            row_list.append(row[1])
            row_list.append(row[2])
            tweet_text = row[0]
            tweet_text_list = tweet_text.split()
            for word in tweet_text_list:
                word = strip_punctuation(word)
                if word in positive_words:
                    positive_count+=1
                if word in negative_words:
                    negative_count+=1
            
            row_list.append(positive_count)
            row_list.append(negative_count)
            row_list.append(positive_count - negative_count)
            result_list.append(row_list)



    with open ('resulting_data.csv' , 'w') as input_file:
        csvwriter = csv.writer(input_file)
        csvwriter.writerow(fields)
        for line in result_list:
            csvwriter.writerow(line)
