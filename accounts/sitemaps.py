from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewsSitemap(Sitemap):

    def items(self):
        return ['aboutUs','accounts:loginpage']

    def location(self, item):
        return reverse(item)