from django.contrib import admin
from . import models

@admin.register(models.Chef)
class Chef(admin.ModelAdmin):
    pass

@admin.register(models.Contactus)
class ContactDetails(admin.ModelAdmin):
    list_display = ['fullname', 'subject', 'date']

@admin.register(models.MenuItems)
class MenuItems(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'status', 'date']
    search_fields = ['title', 'status', 'date']
    actions = ['status_active', 'status_inactive']

    def status_active(self, request, queryset):
        queryset.update(status=True)
    status_active.short_description = 'Active'

    def status_inactive(self, request, queryset):
        queryset.update(status=False)

    status_inactive.short_description = 'InActive'


@admin.register(models.MainMenu)
class AdminMainMenu(admin.ModelAdmin):
    list_display = ['name', 'status', 'title']
    search_fields = ['name', 'title']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    actions = ['status_active', 'status_inactive']

    def status_active(self, request, queryset):
        queryset.update(status=True)

    status_active.short_description = 'Active'

    def status_inactive(self, request, queryset):
        queryset.update(status=False)

    status_inactive.short_description = 'InActive'
