from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from competitors.models import Competitor


def show(request):
    competitors = Competitor.objects.order_by('publication_date')
    t = get_template('competitors/competitors.html')
    html = t.render(Context({'competitors': competitors}))
    return HttpResponse(html)
