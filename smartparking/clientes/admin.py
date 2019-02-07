from django.contrib import admin
from .models import Cliente
from .models import Tel

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Tel)