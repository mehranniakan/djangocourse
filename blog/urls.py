from django.urls import path
from blog.views import home_blog, single_blog, search_blog

urlpatterns = [
    path('', home_blog, name='home_blog'),
    path('Single/<int:pid>', single_blog, name='single_blog'),
    path('Categorys/<str:catname>', home_blog, name='blog_categorys'),
    path('Tags/<str:tagname>', home_blog, name='blog_tags'),
    path('Search', search_blog, name='blog_search'),
    path('AuthorsPosts/<str:auth_name>', home_blog, name='blog_authors')
]
