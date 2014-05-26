from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from news.models import News


def news(request):
    news = News.objects.order_by('publication_date')
    t = get_template('news.html')
    html = t.render(Context({'news': news}))
    return HttpResponse(html)
