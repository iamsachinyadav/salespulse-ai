from django.http import JsonResponse  # type: ignore[import]
from django.db.models import F, Sum
from apps.sales.models import Sale
from apps.social.models import SocialPost
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# ✅ AI TEXT INSIGHTS
def insights_view(request):
    total_sales = Sale.objects.count()
    positive = SocialPost.objects.filter(sentiment="positive").count()

    if positive > 5 and total_sales > 0:
        message = "Positive sentiment and strong revenue. Scale marketing and inventory."
        insight_type = "success"
    else:
        message = "Mixed signals. Monitor sentiment and optimize campaigns."
        insight_type = "warning"

    return JsonResponse({
        "insights": [
            {
                "type": insight_type,
                "message": message
            }
        ]
    })


# ✅ ANALYTICS (CHART DATA)
def analytics_view(request):
    revenue = (
        Sale.objects
        .annotate(amount=F("price") * F("quantity"))
        .aggregate(total=Sum("amount"))["total"] or 0
    )

    sentiments = {
        "positive": SocialPost.objects.filter(sentiment="positive").count(),
        "neutral": SocialPost.objects.filter(sentiment="neutral").count(),
        "negative": SocialPost.objects.filter(sentiment="negative").count(),
    }

    return JsonResponse({
        "revenue": revenue,
        "sentiments": sentiments
    })

# ✅ RECOMMENDATIONS


def recommendations_view(request):
    total_revenue = (
        Sale.objects
        .annotate(amount=F("price") * F("quantity"))
        .aggregate(total=Sum("amount"))["total"] or 0
    )

    positive = SocialPost.objects.filter(sentiment="positive").count()
    negative = SocialPost.objects.filter(sentiment="negative").count()

    recommendations = []

    # Rule 1: Strong growth signal
    if positive >= 5 and total_revenue > 50000:
        recommendations.append({
            "title": "Scale Marketing Spend",
            "action": "Increase ad budget on high-performing channels",
            "priority": "HIGH",
            "confidence": 0.86
        })

    # Rule 2: Negative sentiment warning
    if negative >= 3:
        recommendations.append({
            "title": "Address Customer Issues",
            "action": "Review recent complaints and fix product issues",
            "priority": "HIGH",
            "confidence": 0.78
        })

    # Rule 3: Default suggestion
    if not recommendations:
        recommendations.append({
            "title": "Monitor Performance",
            "action": "Collect more data before making strategic changes",
            "priority": "MEDIUM",
            "confidence": 0.55
        })

    return JsonResponse({
        "recommendations": recommendations
    })

@api_view(["GET"])
def analytics_view(request):
    data = {
        "totalRevenue": 0,
        "sentiment": {
            "positive": 0,
            "negative": 0,
            "neutral": 0
        }
    }
    return Response(data)


def recommendations_view(request):
    recommendation = {
        "title": "Monitor Performance",
        "message": "Collect more data before making strategic changes",
        "priority": "MEDIUM",
        "confidence": 55
    }
    return JsonResponse(recommendation)
