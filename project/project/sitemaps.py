from django.contrib.sitemaps import Sitemap
from ex_items.models import Experience
from django.urls import reverse

class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'
    limit = 50000

    def items(self):
        experience = Experience.objects.filter(active=True, active_admin=True)
        return experience

    def location(self,obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.timestamp


#You can also add static pages such as home to your dynamic Django sitemap
class HomeSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    protocol = 'https'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)


#You can also add static pages such as /contact or /about to your dynamic Django sitemap
class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.2
    protocol = 'https'

    def items(self):
        return ['EX-settings:cooperation', 'EX-settings:about-us', 'EX-account:register', 'EX-account:login', 'EX-contact:contact-us']

    def location(self, item):
        return reverse(item)