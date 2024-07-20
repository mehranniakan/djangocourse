from django import template
from django.utils import timezone

from blog.models import Post, Category, Comment

register = template.Library()


@register.simple_tag()
def views_counter(pid):
    current_date = timezone.now().date()
    query = Post.objects.get(id=pid, Status=True, Publish_date__lte=current_date)
    return query.Counted_Views


@register.filter()
def text_sniper(txt):
    val = str(txt).split()[:50]
    val = list(val)
    val = ' '.join(val)
    return val + '...'


@register.inclusion_tag('blog/LatestPosts.html')
def latest_posts(count=3):
    current_date = timezone.now().date()
    query = Post.objects.filter(Status=True, Publish_date__lte=current_date).order_by('-Publish_date')[:count]
    return {'Posts': query}


@register.inclusion_tag('blog/PostCategorys.html')
def Post_Category():
    current_date = timezone.now().date()
    posts = Post.objects.filter(Status=True, Publish_date__lte=current_date)
    category = Category.objects.all()
    cat_dict = {}
    for name in category:
        cat_dict[name] = posts.filter(Category=name).count()
    return {'Categories': cat_dict}


@register.simple_tag(name='comments_count')
def comments_count(pid):
    return Comment.objects.filter(Approved=True, pk=pid).count()

