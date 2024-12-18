from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from backoffice.models import Author, Publisher, Title, Reservation
from backoffice.forms import LoginForm, SignUpForm, ReservationForm
from django.core.paginator import Paginator


def home(request):
    return render(request, 'home.html')


def books(request):
    books = Title.objects.order_by('title')
    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'books.html', {'page_object': page_object})


def bookDetails(request, title_id):
    book = Title.objects.get(title_id=title_id)
    publisher = Publisher.objects.get(pubid=book.pubid.pubid)

    return render(request, 'bookDetails.html', {'book': book, 'publisher': publisher })


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


def publisherDetails(request, pubid):
    publisher = get_object_or_404(Publisher, pubid=pubid)

    return render(request, 'publisherDetails.html', {'publisher': publisher})


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
    messages = None
    user = logout(request)
    return redirect('home')


def reservation(request, title_id):
    book = Title.objects.get(title_id=title_id)
    error = None
    success = None
    info = None

    # verify if user is connected to render the form only if true
    if request.user.is_authenticated :
        user = request.user

        # Get user reservation to limit to 3 books at the same time
        reservations = Reservation.objects.filter(user=user)

        if len(reservations) > 2:
            info = "Vous ne pouvez pas réserver plus de 3 livres en même temps."

        if request.method == 'POST':
            form = ReservationForm(request.POST)

            if form.is_valid():
                start_date = request.POST['start_date']
                title = Title.objects.get(title_id=title_id)
                status = True

                reservation = Reservation(start_date=start_date, title=title, user=user)
                reservation.save()

                Title.objects.filter(title_id=title_id).update(status=status)
                success = "Votre réservation a bien été ajoutée !"
                
            else :
                error = "Une erreur est survenue, veuillez réessayer ou vérifier les informations."

    else:
        form = ReservationForm()
        info = "Vous devez vous connecter pour réserver un livre."

    return render(request, 'reservation.html', {'form': form, 'book': book, 'error': error, 'success': success, 'info': info })


def profile(request):
    return render(request, 'profile.html')

