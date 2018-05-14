from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

from TEST.models import sala, jugador

@admin.register(sala)
class AdminSala(ImportExportActionModelAdmin,admin.ModelAdmin):
    pass

@admin.register(jugador)
class AdminJugador(ImportExportActionModelAdmin,admin.ModelAdmin):
    pass