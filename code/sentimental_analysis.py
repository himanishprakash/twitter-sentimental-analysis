# all the libraries which are need for the project

import pandas as pd
import re
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from wordcloud import WordCloud
from collections import defaultdict




def data_processing(text):
    text = text.lower()
    text = re.sub(r"https\S+|www\S+https\S+", '',text, flags=re.MULTILINE)
    text = re.sub(r'\@w+|\#','',text)
    text = re.sub(r'[^\w\s]','',text)
    text_tokens = word_tokenize(text)
    filtered_text = [w for w in text_tokens if not w in stop_words]
    return " ".join(filtered_text)



def sentiment(label):
    if label <0:
        return "Negative"
    elif label ==0:
        return "Neutral"
    elif label>0:
        return "Positive"
    
def stemming(data):
    stemmer = PorterStemmer()
    text = [stemmer.stem(word) for word in data]
    return data

def polarity(text):
    return TextBlob(text).sentiment.polarity

def sentimental_analysis(df):
    df_text= pd.DataFrame()
    df_text['text'] = df['text']
    df_text['text'] = df_text['text'].apply(data_processing)
    text_df = df_text.drop_duplicates()
    
    

    
    text_df['text'] = text_df['text'].apply(lambda x: stemming(x))
    
    
    
    text_df['polarity'] = text_df['text'].apply(polarity)
    

        
    text_df['sentiment'] = text_df['polarity'].apply(sentiment)
    
    return text_df



def plots(df, df_2):
    # Plotting Average views count per Hashtag
    df= df.dropna(subset = ['hashtag'])
    plt.bar(df['hashtag'], df['views_count'], color='skyblue')

    # Adding title and labels
    plt.title('Average views count per Hashtag')
    plt.xlabel('Hashtag')
    plt.ylabel('Average views count')

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Display the plot
    plt.tight_layout()
    plt.show()
    hashtag_plot_filename = 'hashtag_plot.png'
    plt.savefig(hashtag_plot_filename)
    plt.clf()
    plt.show()

    # Plotting Distribution of sentiments
    fig = plt.figure(figsize=(7,7))
    colors = ("yellowgreen", "gold", "red")
    wp = {'linewidth':2, 'edgecolor':"black"}
    tags = df_2['sentiment'].value_counts()
    explode = (0.1,0.1,0.1)
    tags.plot(kind='pie', autopct='%1.1f%%', shadow=True, colors = colors,
            startangle=90, wedgeprops = wp, explode = explode, label='')
    plt.title('Distribution of sentiments')
    
def wordcloud(df):
    word_sentiment = defaultdict(list)
    for _, row in df.iterrows():
        words = row['text'].split()
        for word in words:
            word_sentiment[word].append(row['polarity'])

    # Calculate average sentiment for each word
    word_avg_sentiment = {word: sum(sentiments) / len(sentiments) for word, sentiments in word_sentiment.items()}

    # Define a function to determine the color of words in the word cloud
    def color_func(word, **kwargs):
        return "green" if word_avg_sentiment.get(word, 0) > 0 else "red"

    # Generate word cloud
    text = ' '.join(df['text'])
    wordcloud = WordCloud(width=800, height=400).generate(text)

    # Display the generated image with the color function applied
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud.recolor(color_func=color_func), interpolation='bilinear')
    plt.axis('off')
    plt.show()
    
    
def main():
    extracted_data = pd.read_csv('extracted_df.csv')
    top_10 = pd.read_csv('top_10.csv')
    extract_data = sentimental_analysis(extracted_data)

    # Create and show the plots
    plots(top_10, extract_data)
    wordcloud(extract_data)
    
    
if __name__ == "__main__":
    main()
    
    
