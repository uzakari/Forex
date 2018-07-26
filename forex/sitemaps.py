from django.contrib.sitemaps import Sitemap

from .models import Comment

from django.urls import reverse


class CommentSitemaps(Sitemap):

    def items(self):
        return Comment.objects.all()


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['about', 'pricing', 'services', 'register', 'payment', 'weather']

    def location(self, obj):
        return reverse(obj)