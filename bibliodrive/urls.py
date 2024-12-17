"""
URL configuration for bibliodrive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backoffice import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('livres/', views.books, name='books'),
    path('livres/<int:title_id>', views.bookDetails, name='book'),
    path('livres/<int:title_id>/reservation', views.reservation, name='reservation'),
    path('auteurs/', views.authors, name='authors'),
    path('auteurs/<int:au_id>', views.authorDetails, name='author'),
    path('editeurs/', views.publishers, name='publishers'),
    path('editeurs/<int:pubid>', views.publisherDetails, name='publisher'),
    path('inscription/', views.registration, name='registration'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('profil/', views.profile, name='profile')
] + static(settings.IMAGES_URL, document_root=settings.IMAGES_ROOT)
