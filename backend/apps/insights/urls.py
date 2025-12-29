from django.urls import path
from .views import insights_view, analytics_view, recommendations_view

urlpatterns = [
    path("", insights_view),              # /api/insights/
    path("analytics/", analytics_view),    # /api/insights/analytics/
    path("recommendations/", recommendations_view),  # /api/insights/recommendations/
]

