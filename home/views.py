from django.shortcuts import render, get_object_or_404
from .models import Book, Author
from django.core.paginator import Paginator
from django.db.models import Q

books_per_page = 4

def book_list(request):
    books = Book.objects.all()

    paginator = Paginator(books, books_per_page)
    page_number = request.GET.get('page')
    if(page_number == None):
        page_number = 1


    query = request.GET.get('query')
    if(query == None):
        query = "" 

    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'authors':Author.objects.all()}
    return render(request, 'home/index.html', context)


def book_search(request):
    query = request.GET.get('query')
    author = request.GET.get('author')
    if(author == "" or author == None):
        books = Book.objects.filter(Q(title__contains = query)).values() | Book.objects.filter(Q(description__contains = query)).values()
    else:
        books = Book.objects.filter(Q(title__contains = query, author__name__contains = author)).values() | Book.objects.filter(Q(author__slug__contains = author)).values() | Book.objects.filter(Q(description__contains = query, author__name__contains = author)).values()

    paginator = Paginator(books, books_per_page)
    page_number = request.GET.get('page')
    if(page_number == None):
        page_number = 1
    
    if(query == None):
        query = "" 

    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, "query": query, 'authors':Author.objects.all(), 'author_filter': author}
    return render(request, 'home/search.html', context)




def book_details(request, slug):
    book = get_object_or_404(Book, slug=slug,)
    context = {'book': book}
    query = request.GET.get('query')
    if(query == None):
        query = "" 
    return render(request, 'home/details.html', context)


