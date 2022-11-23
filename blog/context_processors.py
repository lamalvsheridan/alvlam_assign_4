from django.db.models import Count

from . import models


def base_context(request):
    topics = models.Topic.objects.annotate(Count('blog_posts')).order_by('-blog_posts__count')[:10]

    return {'topics': topics}
