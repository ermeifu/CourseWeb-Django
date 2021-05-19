from django.contrib import admin

# Register your models here.
from .models import Menu, Home, ReferenceBooks, TeachingResources, HomeImages, CourseMessage


class MenuManager(admin.ModelAdmin):
    list_display = ['id', 'pattern', 'parentId', 'enabled', 'name', 'component']
    list_display_links = ['id']
    list_filter = ['enabled']
    search_fields = ['name']
    list_editable = ['name']


admin.site.register(Menu, MenuManager)
# admin.site.register(Home)
admin.site.register(CourseMessage)
admin.site.register(HomeImages)
admin.site.register(TeachingResources)
admin.site.register(ReferenceBooks)


