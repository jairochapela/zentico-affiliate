from django.db import models

# Create your models here.

class AffiliateLink(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    advertiser = models.CharField(max_length=200)
    target_url = models.URLField()
    clicks = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)