from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    artistic_name = models.CharField(max_length=64, null=True, blank=True)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.name


class Band(models.Model):

    GENRE_NOT_DEFINED = -1
    GENRE_ROCK = 0
    GENRE_METAL = 1
    GENRE_POP = 2
    GENRE_HIPHOP = 3
    GENRE_ELECTRONIC = 4
    GENRE_REGGAE = 5
    GENRE_OTHER = 6

    GENRES = (
        (GENRE_NOT_DEFINED, "not defined"),
        (GENRE_ROCK, "rock"),
        (GENRE_METAL, "metal"),
        (GENRE_POP, "pop"),
        (GENRE_HIPHOP, "hip-hop"),
        (GENRE_ELECTRONIC, "electronic"),
        (GENRE_REGGAE, "reggae"),
        (GENRE_OTHER, "other"),
    )

    name = models.CharField(max_length=128, unique=True)
    persons = models.ManyToManyField(Person, related_name="bands")
    genre = models.IntegerField(default=-1, choices=GENRES)

    def __str__(self):
        return self.name


class ConcertCity(models.Model):
    name = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name


class RealConcert(models.Model):
    name = models.CharField(max_length=128)
    persons = models.ManyToManyField(Person, related_name="real_concerts")
    bands = models.ManyToManyField(Band, related_name="real_concerts", blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    place = models.CharField(max_length=128)
    city = models.ForeignKey(
        ConcertCity, on_delete=models.PROTECT, related_name="real_concerts"
    )
    description = models.TextField(null=True, blank=True)
    facebook_page = models.URLField(max_length=250, null=True, blank=True)
    likes = models.ManyToManyField("auth.User", related_name="real_concerts_likes")

    def __str__(self):
        return self.name


class DreamConcert(models.Model):
    persons = models.ManyToManyField(Person, related_name="dream_concerts")
    bands = models.ManyToManyField(Band, related_name="dream_concerts")
    city = models.ForeignKey(ConcertCity, on_delete=models.PROTECT)
    likes = models.ManyToManyField("auth.User", related_name="dream_concerts_likes")
