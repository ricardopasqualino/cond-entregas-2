from django.contrib import admin

from delivery.models import ( 
    Delivery, 
    Casa, 
    Box,
    Morador,
    )


class CasaAdmin(admin.ModelAdmin):
    list_display = ['numero', 'rua', 'moradores']


class MoradorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'telefone', 'email']


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['id', 'nota_fiscal', 'data_entrada', 'recebido_por', 'casa', 'modulo', 'status']


admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Casa, CasaAdmin)
admin.site.register(Box)
admin.site.register(Morador, MoradorAdmin)