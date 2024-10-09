from django.contrib import admin
from .models import PortfolioItem

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('created_at',)


admin.site.register(PortfolioItem, PortfolioAdmin)