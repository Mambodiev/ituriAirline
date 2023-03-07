from django.contrib import admin
from .models import Ticket, OrderItem, Order, Address


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'civilité',
        'prénom',
        'nom_de_famille',
        'address_type',
    ]

admin.site.register(Address, AddressAdmin)
admin.site.register(Ticket)
admin.site.register(OrderItem)
admin.site.register(Order)
