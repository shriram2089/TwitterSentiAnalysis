
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import nltk

nltk.download('vader_lexicon')

def analyze_sentiment(df):
    """
    Analyze sentiment of tweets using VADER.
    """
    sid = SentimentIntensityAnalyzer()
    df['Sentiment'] = df['Tweet'].apply(lambda x: sid.polarity_scores(x)['compound'])
    df['Sentiment_Label'] = df['Sentiment'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))
    return df
