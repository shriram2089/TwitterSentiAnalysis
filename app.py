import pandas as pd
from data_fetcher import fetch_tweets
from sentiment_analysis import analyze_sentiment
from visualization import plot_sentiment_distribution, plot_trend_analysis

def main():
    # Configuration
    API_KEY = 'YOUR_TWITTER_API_KEY'
    API_SECRET_KEY = 'YOUR_TWITTER_API_SECRET_KEY'
    ACCESS_TOKEN = 'YOUR_TWITTER_ACCESS_TOKEN'
    ACCESS_TOKEN_SECRET = 'YOUR_TWITTER_ACCESS_TOKEN_SECRET'
    QUERY = 'Python'
    MAX_TWEETS = 500
    
    # Fetch data
    df = fetch_tweets(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, QUERY, MAX_TWEETS)
    
    # Perform sentiment analysis
    df = analyze_sentiment(df)
    
    # Plot results
    plot_sentiment_distribution(df)
    plot_trend_analysis(df)

if __name__ == "__main__":
    main()
