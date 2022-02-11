from django.shortcuts import render, redirect

# Create your views here.
from .models import BookList


def index(request):
    books = BookList.objects.all()
    return render(request, 'index.html', {'books': books})


def create(request):
    print(request.POST)
    title = request.GET('title')
    price = request.GET('price')
    author = request.GET('author')
    book_details  = BookList(title=title, price=price, author=author)
    book_details.save()
    return redirect('/')


def add_book(request):
    context = {

    }
    request render(request, 'add_book.html', context)


def delete(request, id):
    books = BookList.objects.get(pk=id)
    books.delete()
    return redirect('/')


def edit(request, id):
    books = BookList.objects.get(pk=id)
    context = {
        'books': books
    }
    return render(request, 'edit.html', context)


def update(request, id):
    books = BookList.objects.get(pk=id)
    books.title = request.GET['title']
    books.price = request.GET['price']
    books.author = request.GET['author']
    books.save()
    return redirect('/')
