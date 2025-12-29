from apps.sales.models import Sale
from apps.social.models import SocialPost
from django.db.models import Avg, Sum, F, ExpressionWrapper, FloatField


def generate_insights():
    insights = []

    # --- Revenue calculation (price * quantity) ---
    revenue_expression = ExpressionWrapper(
        F("price") * F("quantity"),
        output_field=FloatField()
    )

    total_revenue = (
        Sale.objects
        .annotate(revenue=revenue_expression)
        .aggregate(total=Sum("revenue"))["total"] or 0
    )

    avg_revenue = (
        Sale.objects
        .annotate(revenue=revenue_expression)
        .aggregate(avg=Avg("revenue"))["avg"] or 0
    )

    # --- Social Sentiment Counts ---
    positive = SocialPost.objects.filter(sentiment="positive").count()
    negative = SocialPost.objects.filter(sentiment="negative").count()

    # --- Business Rules ---
    if negative > positive:
        insights.append({
            "type": "alert",
            "message": "Negative sentiment is higher than positive. Investigate product quality or customer support."
        })

    if positive > negative and total_revenue < avg_revenue:
        insights.append({
            "type": "opportunity",
            "message": "Positive sentiment but revenue is low. Improve conversion or run promotions."
        })

    if positive > negative and total_revenue > avg_revenue:
        insights.append({
            "type": "success",
            "message": "Positive sentiment and strong revenue. Scale marketing and inventory."
        })

    if not insights:
        insights.append({
            "type": "info",
            "message": "Not enough data to generate strong insights yet."
        })

    return insights
