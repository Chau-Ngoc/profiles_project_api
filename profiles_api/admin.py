from django.contrib import admin
from profiles_api.models import UserProfile, Feed


class FeedAdmin(admin.ModelAdmin):
    readonly_fields = ["created_on"]


admin.site.register(UserProfile)
admin.site.register(Feed, FeedAdmin)
