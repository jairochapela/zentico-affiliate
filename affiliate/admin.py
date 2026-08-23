from django.contrib import admin

from affiliate.models import AffiliateLink

# Register your models here.

@admin.register(AffiliateLink)
class AffiliateLinkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "advertiser",
        "clicks",
        "active",
        "created_at",
    )
    list_filter = ("active", "advertiser")
    search_fields = ("name", "advertiser", "slug")
    prepopulated_fields = {"slug": ("name",)}