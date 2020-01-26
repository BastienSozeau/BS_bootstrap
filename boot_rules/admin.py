from django.contrib import admin
from boot_rules.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title',]


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
