from django.http import HttpResponse

from myapp.models import PhraseOfTheDay


def index(request):
    phrase = PhraseOfTheDay.objects.all()[0].phrase
    return HttpResponse(phrase)
