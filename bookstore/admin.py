from django.contrib import admin
from .models import Book, UserRequest

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at']
    search_fields = ['title']
    list_filter = ['uploaded_at']

admin.site.register(Book, BookAdmin)
admin.site.register(UserRequest)


# Customize the admin panel appearance
admin.site.site_header = 'Maiywa Admin Panel'
admin.site.site_title = 'Maiywa  Admin'
admin.site.index_title = 'Welcome to Maiywa Administration'