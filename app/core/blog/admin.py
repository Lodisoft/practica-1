from django.contrib import admin
from core.blog.models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.
#admin.site.register(Tag)
##admin.site.register(Category)
##admin.site.register(Comment)
##admin.site.register(Profile)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'photo')
    list_display_links = ('pk', 'user',)
    list_editable = ('photo',)

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'updated_on',
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'photo', 'website'),),
        }),
        ('Extra info', {
            'fields': (('updated_on'),),
        })
    )

    readonly_fields = ('updated_on',)

#REGISTRAR PERFIL NUEVO Y USUARIO
class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
#REGISTRAR PERFIL NUEVO Y USUARIO
@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin."""

    list_display = ('id', 'name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin."""

    list_display = ('id', 'name')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'image_header')
    search_fields = ('title', 'user__username', 'user__email')
    list_filter = ('created', 'updated')
        
        
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ('url', )
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        form.base_fields['profile'].initial = request.user.profile
        return form
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'comment')