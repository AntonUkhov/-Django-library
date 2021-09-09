from django.contrib import admin
from .models import Author, Ganre, Book, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Ganre)
admin.site.register(BookInstance)



