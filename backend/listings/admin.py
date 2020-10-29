from django.contrib import admin
from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'kWh', 'price', 'list_date', 'staff')
    list_display_links = ('id', 'title')
    list_filter = ('staff', )
    list_editable = ('is_published', )
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price','kWh')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)