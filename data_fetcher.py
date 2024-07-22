import tweepy
import pandas as pd

def fetch_tweets(api_key, api_secret_key, access_token, access_token_secret, query, max_tweets=100):
    """
    Fetch tweets using Tweepy.
    """
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en").items(max_tweets)
    data = [[tweet.created_at, tweet.text] for tweet in tweets]
    df = pd.DataFrame(data, columns=['Timestamp', 'Tweet'])
    
    return df
