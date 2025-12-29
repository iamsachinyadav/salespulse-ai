from textblob import TextBlob

def analyze_sentiment(text: str) -> str:
    """
    Returns: positive | negative | neutral
    """
    if not text:
        return "neutral"

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    return "neutral"
