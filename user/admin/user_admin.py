from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm as DjangoUserChangeForm
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django.utils.translation import gettext_lazy as _

from user.models import User


# Forms
# ----------------------------------------------------------------------------
class UserCreationForm(DjangoUserCreationForm):
    class Meta:
        model = User
        fields = ['email']


class UserChangeForm(DjangoUserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


# ModelAdmins
# ----------------------------------------------------------------------------
@admin.register(User)
class UserAdmin(AuthUserAdmin):
    add_form_template = 'admin/auth/user/add_form.html'
    model = User
    readonly_fields = ['uuid', 'date_joined', 'last_login', 'created_at', 'created_by', 'modified_at', 'modified_by']
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['email', 'first_name', 'last_name', 'is_active']
    list_filter = ['is_superuser', 'is_active']
    search_fields = ['first_name', 'last_name', 'email']
    ordering = ['email']

    fieldsets = [
        [_('Information'), {'fields': ['email', 'first_name', 'last_name', 'uuid', 'language']}],
        [_('Permissions'), {'fields': ['is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']}],
        [_('Important dates'), {'fields': ['last_login', 'date_joined']}],
        [_('Password'), {'fields': ['password']}],
        [_('Creation and modification'), {'fields': ['created_at', 'created_by', 'modified_at', 'modified_by']}]
    ]

    add_fieldsets = [
        [None, {'classes': ['wide'], 'fields': ['email', 'password1', 'password2']}]
    ]
