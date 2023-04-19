from django.contrib import admin

# Register your models here.
from .models import Categoria
from .models import Producto
from .models import Cliente


admin.site.register(Categoria)

#admin.site.register(Producto)
@admin.register(Producto)
class Producto(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock', 'categoria')
    list_display_links = ('id',)
    list_editable = ('nombre', 'precio', 'stock')
    search_fiels = ('nombre',)
#admin.site.register(Cliente)
@admin.register(Cliente)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'dni', 'telefono', 'direccion', 'email', 'fecha_nacimiento', 'fecha_publicacion')
    list_display_links = ('id',)
    list_editable = ('nombres', 'apellidos', 'dni', 'telefono', 'direccion', 'email', 'fecha_nacimiento')
    search_fields = ('nombres', 'apellidos', 'dni', 'telefono', 'email')
    