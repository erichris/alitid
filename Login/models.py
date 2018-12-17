from django.db import models
from django.contrib import admin
from datetime import datetime

# Create your models here.
class PlanEscape(models.Model):
    ID1 = models.CharField(max_length=20, verbose_name = "Usuario")
    ID2 = models.CharField(max_length=20, verbose_name = "Password")
    created = models.DateTimeField(default =datetime.now() , verbose_name = "Fecha de creacion")
    used = models.BooleanField(default = False, verbose_name = "Se ha usado?");
    app = models.CharField(max_length=50, default = "PlanDeEscape", verbose_name = "Aplicacion destino")
    ID_Movil1 = models.CharField(max_length=50, blank = True, verbose_name = "ID movil 1")
    ID_Movil2 = models.CharField(max_length=50, blank = True, verbose_name = "ID movil 2")
    ID_Movil3 = models.CharField(max_length=50, blank = True, verbose_name = "ID movil 3")
    
    def __str__(self):
        return u'%s %s' % (self.ID1, self.ID2)
    
class PlanEscapeAdmin(admin.ModelAdmin):
    list_display = ('ID1', 'ID2', 'used', 'app', 'created')