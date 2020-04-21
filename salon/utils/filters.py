from django.contrib.postgres.search import TrigramSimilarity
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.functions import Greatest
from rest_framework.filters import BaseFilterBackend


class TrigramSearchFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        searchkey = request.query_params.get('tgsearch')
        if not searchkey:
            return queryset

        trigram = TrigramSimilarity(view.tgsearch_field, searchkey)
        return queryset.annotate(similarity=trigram).filter(
            similarity__gt=view.tgsearch_threshold).order_by('-similarity')
