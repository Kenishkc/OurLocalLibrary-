
# Register your models here.
from django.contrib import admin
from .models import Author, Genre, Book, BookInstance ,UserProfile,BorrowedBook


class AuthorAdmin(admin.ModelAdmin):
    list_display = ( 'first_name','last_name', 'date_of_birth')

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
     list_display = ('title', 'author', 'display_genre')  # Update the list_display

     def display_genre(self, obj):
        return ', '.join([genre.name for genre in obj.genre.all()])

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

#admin.site.register(Book)
# # admin.site.register(Author)

admin.site.register(Genre)
#admin.site.register(BookInstance)

admin.site.register(UserProfile)

admin.site.register(BorrowedBook)