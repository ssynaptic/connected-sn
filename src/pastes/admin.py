from django.contrib import admin
from pastes.models import (User, Paste, PasteView,
    Comment, Like, Dislike)
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Paste)
admin.site.register(PasteView)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Dislike)