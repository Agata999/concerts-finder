"""events_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from concerts.views import LandingPage, MainPage, ChooseFinder, BandConcertsFinder, ArtistConcertsFinder, \
    DateConcertsFinder, CityConcertsFinder, ConcertDetails, TopConcerts, LikeRealConcert, ListOfDreamConcerts, \
    SearchDreamConcert, LikeDreamConcert, AddDreamConcert, LoginView, LogoutView, RegisterUserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name='loading-page'),
    path('main/', MainPage.as_view(), name='main-page'),
    path('choose_finder/', ChooseFinder.as_view(), name='choose-finder'),
    path('band_concerts_finder/', BandConcertsFinder.as_view(), name='band-concerts-finder'),
    path('artist_concerts_finder/', ArtistConcertsFinder.as_view(), name='artist-concerts-finder'),
    path('date_concerts_finder/', DateConcertsFinder.as_view(), name='date-concerts-finder'),
    path('city_concerts_finder/', CityConcertsFinder.as_view(), name='city-concerts-finder'),
    re_path(r'^concert_details/(?P<id>(\d)+)', ConcertDetails.as_view(), name='concert-details'),
    path('top10/', TopConcerts.as_view(), name='top-concerts'),
    re_path(r'^like_realconcert/(?P<id>(\d)+)', LikeRealConcert.as_view(), name='realconcert-likes'),
    path('list_of_dreamconcerts/', ListOfDreamConcerts.as_view(), name='list-of-dreamconcerts'),
    path('search_dreamconcert/', SearchDreamConcert.as_view(), name='search-dreamconcert'),
    re_path(r'^like_dreamconcert/(?P<id>(\d)+)', LikeDreamConcert.as_view(), name='dreamconcert-likes'),
    path('add_dreamconcert/', AddDreamConcert.as_view(), name='add-dreamconcert'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register_user')
]
