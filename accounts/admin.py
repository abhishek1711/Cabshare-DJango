from django.contrib import admin
from accounts.models import UserProfile,Post
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = {'user','user_info','city','phone','website'}

    def user_info(self,obj):
        return obj.description

    user_info.short_description = 'Info'

admin.site.register(UserProfile)
admin.site.register(Post)
