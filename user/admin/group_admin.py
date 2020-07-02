from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _


class GroupAdmin(GroupAdmin):
    readonly_fields = ['uuid']

    fieldsets = (
        (_('Information'), {'fields': ['label', 'name', 'uuid']}),
        (_('Permissions'), {'fields': ['permissions']}),
    )


admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
