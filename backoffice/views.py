from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from backoffice.models import Author, Publisher, Title
from backoffice.forms import LoginForm, SignUpForm
from django.core.paginator import Paginator


def home(request):
    publishers = Publisher.objects.all()
    return render(request, 'home.html', {'publishers': publishers, })


def books(request):
    books = Title.objects.order_by('title')
    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'books.html', {'page_object': page_object})


def bookDetails(request, title_id):
    book = Title.objects.get(title_id=title_id)
    publisher = Publisher.objects.get(pubid=book.pubid.pubid)

    return render(request, 'bookDetails.html', {'book': book, 'publisher': publisher})


def authors(request):
    authors = Author.objects.order_by('author')

    paginator = Paginator(authors, 5)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'authors.html', {'page_object': page_object})


def authorDetails(request, au_id):
    author = get_object_or_404(Author, au_id=au_id) 
    books = Title.objects.all().filter(authors=au_id)

    return render(request, 'authorDetails.html', {'author': author, 'books': books })


def publishers(request):
    publishers = Publisher.objects.order_by('name')

    paginator = Paginator(publishers, 5)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'publishers.html', {'page_object': page_object})


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})

def connexion(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    return render(request, 'connexion.html', {'form': form})


def deconnexion(request):
    user = logout(request)
    return redirect('home')


def profile(request):
    return render(request, 'profile.html')