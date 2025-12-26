from django.db import models

class SocialPost(models.Model):
    platform = models.CharField(max_length=50)  # Instagram, Twitter, etc.
    content = models.TextField()
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    sentiment = models.CharField(
        max_length=20,
        default="neutral"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.platform} - {self.sentiment}"
