from django.contrib import admin
from django.utils.html import format_html
from django.shortcuts import render
from django.urls import path, re_path, reverse

from .models import Cart, CartItem

class CartItemAdmin(admin.ModelAdmin):
    model = CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'total', 'cart_session_id', 'cart_actions')
    inlines = [CartItemInline]
    search_fields = ('total', 'pk', 'cart_session_id')

    def initiate_xero_invoice(self, request, pk, *args, **kwargs):
        return self.create_xero_invoice(
            request=request,
            pk=pk,
        )

    def create_xero_invoice(self, request, pk):
        cart = self.get_object(request, pk)
        context = {'cart': cart}

        return render(request, "xero/contact-shipping.html", context)

    def cart_actions(self, obj):
        return format_html(
            '<a class="button" href="{}" target="_blank">Xero Invoice</a>&nbsp;',
            reverse('admin:xero-invoice', args=[obj.pk]),
        )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            re_path(
                r'(?P<pk>.+)/invoice/',
                self.admin_site.admin_view(self.initiate_xero_invoice),
                name='xero-invoice',
            ),
        ]
        return custom_urls + urls


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
