from django.shortcuts import render
from django.views import View
from .models import RealConcert, DreamConcert
from .forms import SearchBandConcertsForm, SearchDreamConcertForm


class LoadingPage(View):
    def get(self, request):
        return render(request, "index.html")


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
        form = SearchDreamConcertForm()
        concerts = DreamConcert.objects.all()
        if "city" in request.GET:
            search_ctx = request.GET["city"]
            concerts = concerts.filter(city=search_ctx)
        # if "bands" in request.GET:
        #     search_ctx = request.GET["bands"]
        #     concerts = concerts.filter(bands=search_ctx)
        if "persons" in request.GET:
            search_ctx = request.GET["persons"]
            concerts = concerts.filter(persons=search_ctx)
        else:
            concerts = None
        return render(request, "search_dream_concert.html", {"form": form,
                                                             "concerts": concerts})

