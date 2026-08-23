from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import AffiliateLink


def home(request):
	links = AffiliateLink.objects.filter(active=True).order_by('name')
	return render(request, 'affiliate/home.html', {'links': links})


def go_to_affiliate(request, slug):
	link = get_object_or_404(AffiliateLink, slug=slug, active=True)
	AffiliateLink.objects.filter(pk=link.pk).update(clicks=F('clicks') + 1)
	return HttpResponseRedirect(link.target_url)
