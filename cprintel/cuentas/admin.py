from django.contrib import admin

from .models import Agregado,Banco


class RGbanco(admin.ModelAdmin):
    list_display = ["nombre","n_cta"]
class RGagregado(admin.ModelAdmin):
    list_display = ["nombre_banco","nombre_proveedor","nombre_banco","n_cta"]
    list_display_links = ["nombre_proveedor"]
    search_fields = ["nombre_banco","nombre_proveedor","n_cta"]
    list_per_page = 20




admin.site.register(Agregado,RGagregado)
admin.site.register(Banco,RGbanco)