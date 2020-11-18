from django.contrib import admin
from .models import *


class ShippingDetailInLine(admin.TabularInline):
    model = ShippingOption


class ShippingZoneAdmin(admin.ModelAdmin):
	model = ShippingZone


class ShippingAdmin(admin.ModelAdmin):
    class Meta:
        model = Shipping

    inlines = [ShippingDetailInLine]

class SuburbAdmin(admin.ModelAdmin):
    class Meta:
        model = Suburb

    list_display = ('postal_code', 'delivery_price')
    search_fields = ('postal_code', 'delivery_price')

class DisallowedShippingDatesAdmin(admin.ModelAdmin):
    class Meta:
        model = DisallowedShippingDates
    
    def dateString(obj):
        return (str(obj.date))
    
    list_display = (dateString, 'state')


admin.site.register(Suburb, SuburbAdmin)
admin.site.register(DisallowedShippingDates, DisallowedShippingDatesAdmin)