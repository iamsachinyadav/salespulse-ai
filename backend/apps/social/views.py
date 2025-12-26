from rest_framework import viewsets
from .models import SocialPost
from .serializers import SocialPostSerializer

class SocialPostViewSet(viewsets.ModelViewSet):
    queryset = SocialPost.objects.all().order_by('-created_at')
    serializer_class = SocialPostSerializer
