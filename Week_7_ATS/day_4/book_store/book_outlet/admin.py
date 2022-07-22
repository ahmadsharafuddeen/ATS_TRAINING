from django.contrib import admin
from .models import Book, Author, Address, Country
# Register your models here.
class AuthorInline(admin.TabularInline):
    model = Author

class AddressAdmin(admin.ModelAdmin):
    inlines = [AuthorInline]
    list_display = ("street", "city", "postal_code")

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("author", "rating")
    list_display = ("title", "author")

class AuthorAdmin(admin.ModelAdmin):
    # inlines = [BookInline, AddressInline]
    list_display = ("first_name", "last_name")
    list_filter = ("first_name", )
    search_fields = ("first_name", )


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country)
