from django.contrib import admin
from .models import Project, Structure

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'slug', 'status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    
class PostAdmin2(admin.ModelAdmin):
    list_display=('full_name', 'post', 'status')
    
admin.site.register(Project, PostAdmin)
admin.site.register(Structure, PostAdmin2)