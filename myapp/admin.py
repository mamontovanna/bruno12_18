from django.contrib import admin
from myapp.models import divans

#class AdminCl(admin.ModelAdmin):
#    list_display = ('Название', 'Цвет', 'Цена')

admin.site.register(divans)


# Register your models here.
