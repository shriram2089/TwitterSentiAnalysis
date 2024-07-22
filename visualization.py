import plotly.express as px

def plot_sentiment_distribution(df):
    """
    Plot sentiment distribution of tweets.
    """
    fig = px.histogram(df, x='Sentiment_Label', title='Sentiment Distribution')
    fig.show()

def plot_trend_analysis(df):
    """
    Plot trend analysis of tweet sentiment over time.
    """
    df['Date'] = pd.to_datetime(df['Timestamp']).dt.date
    sentiment_trend = df.groupby(['Date', 'Sentiment_Label']).size().unstack().fillna(0)
    fig = px.line(sentiment_trend, title='Sentiment Trend Over Time')
    fig.show()
