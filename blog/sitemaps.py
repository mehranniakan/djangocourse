from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.filter(Status=True)

    def lastmod(self, obj):
        return obj.Publish_date

    def location(self, item):
        return reverse('single_blog', kwargs={'pid': item.id})
