from django.db.models import Count
from rest_framework import generics, filters
from cookbookapi3.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ProfileList(generics.ListAPIView):

    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)).order_by('-created_at'
    )
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]
    filterset_fields = [
        'owner__following__followed__profile'
    ]






class ProfileDetail(generics.RetrieveUpdateAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
    posts_count=Count('owner__post', distinct=True),
    followers_count=Count('owner__followed', distinct=True),
    following_count=Count('owner__following', distinct=True)).order_by('-created_at')
    serializer_class = ProfileSerializer