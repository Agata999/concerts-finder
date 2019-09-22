from django.contrib import admin
from .models import RealConcert, DreamConcert, Person, Band, ConcertCity

# Register your models here.
admin.site.register(RealConcert)
admin.site.register(DreamConcert)
admin.site.register(Person)
admin.site.register(Band)
admin.site.register(ConcertCity)
