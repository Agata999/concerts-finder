from django.shortcuts import render
from django.views import View
from .models import RealConcert, DreamConcert
from .forms import SearchBandConcertsForm, SearchDreamConcertForm


class LoadingPage(View):
    def get(self, request):
        samples = RealConcert.objects.all().order_by("likes")[:3]
        return render(request, "index.html", {"samples": samples})


class MainPage(View):
    def get(self, request):
        return render(request, "base.html")


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

