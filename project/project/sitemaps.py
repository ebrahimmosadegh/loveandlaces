from django.contrib.sitemaps import Sitemap
from flowerwall.models import FlowerWall
from promotion.models import Promotion
from django.urls import reverse

class ArticleSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    protocol = 'http'
    limit = 50000

    def items(self):
        flowerwall = FlowerWall.objects.all()
        print('flowerwall: ',flowerwall)
        return flowerwall

    def location(self,obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.timestamp

class PromotionSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    protocol = 'http'
    limit = 50000

    def items(self):
        promotion = Promotion.objects.all()
        return promotion

    def location(self,obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.timestamp

#You can also add static pages such as home to your dynamic Django sitemap
class HomeSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    protocol = 'http'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)


#You can also add static pages such as /contact or /about to your dynamic Django sitemap
class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.2
    protocol = 'http'

    def items(self):
        return ['about', 'contact', 'terms-conditions']

    def location(self, item):
        return reverse(item)