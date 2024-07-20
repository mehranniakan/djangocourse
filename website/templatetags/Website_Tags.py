from django import template
from django.utils import timezone

from blog.models import Post

register = template.Library()


@register.inclusion_tag('web/Latest_Posts_Carousel.html')
def get_latest_post():
    current_date = timezone.now().date()
    lt_posts = Post.objects.filter(Status=True, Publish_date__lte=current_date).order_by('-id')[:6]
    return {'Posts': lt_posts}
