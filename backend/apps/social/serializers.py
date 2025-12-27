from rest_framework import serializers
from .models import SocialPost, analyze_sentiment

class SocialPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPost
        fields = "__all__"
        read_only_fields = ("sentiment", "created_at")

    def create(self, validated_data):
        # FORCE sentiment calculation
        content = validated_data.get("content", "")
        validated_data["sentiment"] = analyze_sentiment(content)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        content = validated_data.get("content", instance.content)
        instance.sentiment = analyze_sentiment(content)
        return super().update(instance, validated_data)
