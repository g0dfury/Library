from django.contrib import admin
from .models import Library, Book, Member, BorrowedBook
# Register your models here.

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'established_date')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'library')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'membership_date', 'email')

# @admin.register(BorrowedBook)
# class BorrowedBookAdmin(admin.ModelAdmin):
#     list_display = ('id', 'member', 'book', 'borrowed_date')



