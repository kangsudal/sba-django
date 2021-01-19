from django.contrib import admin

from .models import Members
class MembersAdmin(admin.ModelAdmin):
    list_display = ('username','useremail')
    pass

admin.site.register(Members, MembersAdmin)
