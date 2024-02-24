from django.contrib import admin
from .models import Cliente, Tel, DOC, Depart

# Register your models here.

class AdminShown(admin.ModelAdmin):
   #fields = ('nome', 'doc','depart','salario','idade','image ')
    list_display =('nome','salario','email')
    list_filter = ('depart',)
    search_fields = ('nome',)



admin.site.register(Cliente,AdminShown)
admin.site.register(Tel)
admin.site.register(DOC)
admin.site.register(Depart)