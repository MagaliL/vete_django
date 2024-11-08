from django.contrib import admin

from .models import Administrador, Cita, Detalle, Dueno, Factura, Paciente, Producto, Usuario, Valoracion, Veterinario



# Register your models here.
admin.site.register(Administrador)
admin.site.register(Cita)
admin.site.register(Detalle)
admin.site.register(Dueno)
admin.site.register(Factura)
admin.site.register(Paciente)
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Valoracion)
admin.site.register(Veterinario)