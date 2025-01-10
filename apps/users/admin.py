from django.contrib import admin

# Register your models here.

from apps.users.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'nick_name', 'birthday']
    search_fields = ['username', 'nick_name', 'birthday']
    list_filter = ['username', 'nick_name', 'birthday']

admin.site.register(UserProfile, UserProfileAdmin)


from apps.users.models import EmailVerifyRecord

class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']

admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


from apps.users.models import Banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

admin.site.register(Banner, BannerAdmin)
