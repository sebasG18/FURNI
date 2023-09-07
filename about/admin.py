from django.contrib import admin
from .models import Content 
# Register your models here.
class ContentAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('title','updated')
    
admin.site.register(Content, ContentAdmin)