from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.db.models import Count
from .models import RealConcert, DreamConcert
from .forms import SearchBandConcertsForm, SearchArtistConcertsForm, SearchDateConcertsForm, SearchDreamConcertForm, \
    SearchCityConcertsForm


class LoadingPage(View):
    def get(self, request):
        samples = RealConcert.objects.all().annotate(likes_count=Count("likes")).order_by("-likes_count")[:3]
        return render(request, "index.html", {"samples": samples})


class MainPage(View):
    def get(self, request):
        concerts = RealConcert.objects.all().order_by("start_date")
        return render(request, "main.html", {"concerts": concerts})


class ChooseFinder(View):
    def get(self, request):
        return render(request, "choose_finder.html")


class BandConcertsFinder(View):
    def get(self, request):
        search = "search" in request.GET
        if search:
            form = SearchBandConcertsForm(request.GET)
            if form.is_valid():
                band_name = form.cleaned_data["name"]
                city = form.cleaned_data["city"]
                start_date = form.cleaned_data["start_date"]
                end_date = form.cleaned_data["end_date"]

                concerts = RealConcert.objects.filter(bands__name__icontains=band_name)

                if city:
                    concerts = concerts.filter(city=city)
                if start_date:
                    concerts = concerts.filter(start_date__date__gte=start_date)
                if end_date:
                    concerts = concerts.filter(start_date__date__lte=end_date)
        else:
            form = SearchBandConcertsForm()
            concerts = None

        return render(request, 'band_concerts_finder.html', {"form": form,
                                                             "concerts": concerts,
                                                             "search": search})


class ArtistConcertsFinder(View):
    def get(self, request):
        search = "search" in request.GET
        if search:
            form = SearchArtistConcertsForm(request.GET)
            if form.is_valid():
                last_name = form.cleaned_data["last_name"]
                artistic_name = form.cleaned_data["artistic_name"]
                city = form.cleaned_data["city"]
                start_date = form.cleaned_data["start_date"]
                end_date = form.cleaned_data["end_date"]

                concerts = RealConcert.objects.all()

                if last_name:
                    concerts = concerts.filter(persons__last_name__icontains=last_name)
                if artistic_name:
                    concerts = concerts.filter(persons__artistic_name__icontains=artistic_name)
                if city:
                    concerts = concerts.filter(city=city)
                if start_date:
                    concerts = concerts.filter(start_date__date__gte=start_date)
                if end_date:
                    concerts = concerts.filter(start_date__date__lte=end_date)
        else:
            form = SearchArtistConcertsForm()
            concerts = None

        return render(request, 'artist_concerts_finder.html', {"form": form,
                                                             "concerts": concerts,
                                                             "search": search})


class DateConcertsFinder(View):
    def get(self, request):
        search = "search" in request.GET
        if search:
            form = SearchDateConcertsForm(request.GET)
            if form.is_valid():
                city = form.cleaned_data["city"]
                start_date = form.cleaned_data["start_date"]
                end_date = form.cleaned_data["end_date"]

                concerts = RealConcert.objects.all()

                if city:
                    concerts = concerts.filter(city=city)
                if start_date:
                    concerts = concerts.filter(start_date__date__gte=start_date)
                if end_date:
                    concerts = concerts.filter(start_date__date__lte=end_date)
        else:
            form = SearchDateConcertsForm()
            concerts = None

        return render(request, 'date_concerts_finder.html', {"form": form,
                                                             "concerts": concerts,
                                                             "search": search})


class SearchDreamConcert(View):
    def get(self, request):
        search = "search" in request.GET
        if search:
            form = SearchDreamConcertForm(request.GET)
            if form.is_valid():
                city = form.cleaned_data["city"]
                band = form.cleaned_data["bands"]
                person = form.cleaned_data["persons"]

                concerts = DreamConcert.objects.all()

                if city:
                    concerts = concerts.filter(city=city)
                if band:
                    concerts = concerts.filter(bands=band)
                if person:
                    concerts = concerts.filter(persons=person)
        else:
            form = SearchDreamConcertForm()
            concerts = None

        return render(request, 'search_dream_concert.html', {"form": form,
                                                             "concerts": concerts,
                                                             "search": search})


class LikeDreamConcert(View):
    def get(self, request, id):
        concert = get_object_or_404(DreamConcert, id=id)
        return render(request, 'like_dream_concert.html', {"concert": concert})

    def post (self, request, id):
        concert = get_object_or_404(DreamConcert, id=id)
        user = request.user
        concert.likes.add(user)
        return redirect("dreamconcert-likes", id=concert.id)


class LikeRealConcert(View):
    def get(self, request, id):
        concert = get_object_or_404(RealConcert, id=id)
        return render(request, 'like_real_concert.html', {"concert": concert})

    def post (self, request, id):
        concert = get_object_or_404(RealConcert, id=id)
        user = request.user
        concert.likes.add(user)
        return redirect("realconcert-likes", id=concert.id)


class ConcertDetails(View):
    def get(self, request, id):
        concert = get_object_or_404(RealConcert, id=id)
        return render(request, 'concert-details.html', {"concert": concert})


class CityConcertsFinder(View):
    def get(self, request):
        search = "search" in request.GET
        if search:
            form = SearchCityConcertsForm(request.GET)
            if form.is_valid():
                city = form.cleaned_data["city"]
                start_date = form.cleaned_data["start_date"]
                end_date = form.cleaned_data["end_date"]

                concerts = RealConcert.objects.filter(city=city)

                if start_date:
                    concerts = concerts.filter(start_date__date__gte=start_date)
                if end_date:
                    concerts = concerts.filter(start_date__date__lte=end_date)
        else:
            form = SearchCityConcertsForm()
            concerts = None

        return render(request, 'city_concerts_finder.html', {"form": form,
                                                             "concerts": concerts,
                                                             "search": search})


class TopConcerts(View):
    def get(self, request):
        concerts = RealConcert.objects.all().annotate(likes_count=Count("likes")).order_by("-likes_count")[:10]
        return render(request, "top_concerts.html", {"concerts": concerts})



