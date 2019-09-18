from django import forms
from .models import ConcertCity, Person, Band


class SearchBandConcertsForm(forms.Form):
    name = forms.CharField(label="Podaj nazwę zespołu", max_length=64, required=False)
    city = forms.ModelChoiceField(label="Jeśli chcesz, wybierz miasto",
                                  widget=forms.Select,
                                  queryset=ConcertCity.objects.all().order_by("name"),
                                  required=False)
    start_date = forms.DateField(label="Jeśli chcesz, wskaż najwcześniejszy termin koncertu",
                                 widget=forms.SelectDateWidget,
                                 required=False)
    end_date = forms.DateField(label="Jeśli chcesz, wskaż najpóźniejszy termin koncertu",
                               widget=forms.SelectDateWidget,
                               required=False)


class SearchArtistConcertsForm(forms.Form):
    last_name = forms.CharField(label="Podaj nazwisko artysty", max_length=64, required=False)
    artistic_name = forms.CharField(label="Lub pseudonim", max_length=64, required=False)
    city = forms.ModelChoiceField(label="Jeśli chcesz, wybierz miasto",
                                  widget=forms.Select,
                                  queryset=ConcertCity.objects.all().order_by("name"),
                                  required=False)
    start_date = forms.DateField(label="Jeśli chcesz, wskaż najwcześniejszy termin koncertu",
                                 widget=forms.SelectDateWidget,
                                 required=False)
    end_date = forms.DateField(label="Jeśli chcesz, wskaż najpóźniejszy termin koncertu",
                               widget=forms.SelectDateWidget,
                               required=False)


class SearchDateConcertsForm(forms.Form):
    start_date = forms.DateField(label="Jeśli chcesz, wskaż najwcześniejszy termin koncertu",
                                 widget=forms.SelectDateWidget,
                                 required=False)
    end_date = forms.DateField(label="Jeśli chcesz, wskaż najpóźniejszy termin koncertu",
                               widget=forms.SelectDateWidget,
                               required=False)
    city = forms.ModelChoiceField(label="Jeśli chcesz, wybierz jeszcze miasto",
                                  widget=forms.Select,
                                  queryset=ConcertCity.objects.all().order_by("name"),
                                  required=False)


class SearchCityConcertsForm(forms.Form):
    city = forms.ModelChoiceField(label="Wybierz miasto",
                                  widget=forms.Select,
                                  queryset=ConcertCity.objects.all().order_by("name"))
    start_date = forms.DateField(label="Jeśli chcesz, wskaż najwcześniejszy termin koncertu",
                                 widget=forms.SelectDateWidget,
                                 required=False)
    end_date = forms.DateField(label="Jeśli chcesz, wskaż najpóźniejszy termin koncertu",
                               widget=forms.SelectDateWidget,
                               required=False)


class SearchDreamConcertForm(forms.Form):
    city = forms.ModelChoiceField(label="Wybierz miasto",
                                  widget=forms.Select,
                                  queryset=ConcertCity.objects.all().order_by("name"),
                                  required=False)
    person = forms.ModelChoiceField(label="Wybierz artystę",
                                     queryset=Person.objects.all().order_by("last_name"),
                                     widget=forms.Select,
                                     required=False)
    band = forms.ModelChoiceField(label="Wybierz zespół",
                                   queryset=Band.objects.all().order_by("name"),
                                   widget=forms.Select,
                                   required=False)


class AddDreamConcertForm(forms.Form):
    city = forms.ModelChoiceField(label="Wybierz miasto",
                                  widget=forms.Select,
                                  queryset=ConcertCity.objects.all().order_by("name"))
    person = forms.ModelChoiceField(label="Wybierz artystę",
                                     queryset=Person.objects.all().order_by("last_name"),
                                     widget=forms.Select,
                                     required=False)
    band = forms.ModelChoiceField(label="Lub zespół",
                                   queryset=Band.objects.all().order_by("name"),
                                   widget=forms.Select,
                                   required=False)


class UserForm(forms.Form):
    username = forms.CharField(label='Podaj login', max_length=64)
    password = forms.CharField(label='Podaj hasło', widget=forms.PasswordInput)


