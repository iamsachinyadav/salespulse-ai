from django.db import models
from textblob import TextBlob


def analyze_sentiment(text):
    if not text:
        return "neutral"

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    return "neutral"

class SocialPost(models.Model):
    platform = models.CharField(max_length=50)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    sentiment = models.CharField(max_length=20, default="neutral")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.platform} - {self.sentiment}"
