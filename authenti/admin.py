from django.contrib import admin, auth


class UserAdmin(admin.ModelAdmin):
   fields = ('username', 'email')
   list_display = ('username', 'email')

admin.site.register(auth.get_user_model(), UserAdmin)
