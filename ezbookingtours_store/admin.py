from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from django.urls import reverse
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.decorators import action

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

class ModelAdminUnfoldBase(ModelAdmin):
    # UI Setup
    compressed_fields = True
    warn_unsaved_form = True
    list_filter_sheet = False
    change_form_show_cancel_button = True
    
    # Row Actions
    actions_row = ["edit"]

    @action(description="Edit", permissions=["change"])
    def edit(self, request, object_id):
        return redirect(reverse(f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change", args=[object_id]))
