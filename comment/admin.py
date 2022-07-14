from django.contrib import admin

from .models import Like, Comment, PostType

class LikeAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "posttype", "post_id"]
    list_display_links = ["id", "post_id"]
    list_filter = ["user", "posttype"]

    search_fields = ["user__username", "posttype__typename", "post_id"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "posttype", "post_id", "comment", "rating", "created_at"]
    list_display_links = ["id", "post_id", "comment"]
    list_filter = ["user", "posttype"]

    search_fields = ["user__username", "posttype__typename", "post_id", "rating"]

class PostTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "typename"]
    list_display_links = ["id", "typename"]

    search_fields = ["typename"]

admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PostType, PostTypeAdmin)
