from django.contrib import admin
from .models import Usuarios,Videos,Comentarios
# Register your models here.
class Usuariolist(admin.ModelAdmin):
    list_display = ('id','Nikename','Usuario')

class Videoslist(admin.ModelAdmin):
    list_display = ('id','Usuario')

class Cometariolist(admin.ModelAdmin):
    list_display = ('id','Usuario')

admin.site.register(Usuarios,Usuariolist)
admin.site.register(Videos,Videoslist)
admin.site.register(Comentarios,Cometariolist)