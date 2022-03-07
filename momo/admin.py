from django.contrib import admin

from momo.models import Cart, CartItem, Momo, MomoCategory

# Register your models here.
admin.site.register(Momo)
admin.site.register(Cart)
admin.site.register(MomoCategory)
admin.site.register(CartItem)