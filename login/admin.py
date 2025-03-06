from django.contrib import admin

from login.models import *

# Register your models here.


admin.site.site_title = "自习室预约管理系统"
admin.site.site_header = "自习室预约管理系统"
admin.site.index_title = "自习室预约管理系统"


class StudentsManager(admin.ModelAdmin):
    # 列表页显示那些字段
    search_fields = ('name', 'phone')
    list_display = ['id', 'name', 'password', 'phone', 'email', 'time', 'is_active', 'admin_sample']


class BookingsManager(admin.ModelAdmin):
    # 列表页显示那些字段
    search_fields = ('students', 'number')
    list_display = ['id', 'students', 'number', 'room', 'period', 'time', 'is_active', 'admin_sample']


class RoomsManager(admin.ModelAdmin):
    # 列表页显示那些字段
    search_fields = ('name',)
    search_fields = ('name',)
    list_display = ['id', 'name', 'number', 'time', 'is_active', 'admin_sample']


class IntegralsManager(admin.ModelAdmin):
    # 列表页显示那些字段
    search_fields = ('student',)
    list_display = ['id', 'student', 'title', 'text', 'time', 'is_active', 'admin_sample']


class TextsManager(admin.ModelAdmin):
    # 列表页显示那些字段
    search_fields = ('title',)
    list_display = ['id', 'title', 'time', 'is_active']


admin.site.register(Students, StudentsManager)
admin.site.register(Rooms, RoomsManager)
admin.site.register(Bookings, BookingsManager)
admin.site.register(Integrals, IntegralsManager)
admin.site.register(Text, TextsManager)
