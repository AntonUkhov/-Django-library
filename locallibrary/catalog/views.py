from django.shortcuts import render
from .models import Book, Author, BookInstance, Ganre
from django.views import generic

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_ganre_fantastic = Ganre.objects.filter(name__iexact='фантастика').count()
    num_books_tolstova = Book.objects.filter(title__iexact='толстова').count()
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors, 'num_ganre_fantastic': num_ganre_fantastic, 'num_books_tolstova': num_books_tolstova},
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book