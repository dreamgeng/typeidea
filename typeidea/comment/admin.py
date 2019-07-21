from django.contrib import admin
from typeidea.custom_site import custom_site
from .models import Comment
from typeidea.base_admin import BaseOwnerAdmin



# Register your models here.
@admin.register(Comment, site=custom_site)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')