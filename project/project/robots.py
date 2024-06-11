from django.http import HttpResponse
from django.views.decorators.http import require_GET


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /*.m3u8",
        "Disallow: /*.ts",
        "Disallow: /favorite-experience/",
        "Disallow: /*?",
        "Disallow: /handle-error/",
        "Disallow: /reset_password/",
        "Disallow: /setting",
        "Disallow: */follow/",
        "Sitemap: https://www.tajrobesaz.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")