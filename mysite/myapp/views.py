import datetime

from django.http import HttpResponse
from kombu import Connection
from django.conf import settings

from myapp.models import PhraseOfTheDay


def index(request):
    phrase = PhraseOfTheDay.objects.all()[0].phrase
    return HttpResponse(phrase)


def produce(request):
    with Connection(settings.RABBITMQ_URL) as conn:
        simple_queue = conn.SimpleQueue('simple_queue')
        message = 'hello rabbit (%s)' % datetime.datetime.today()
        simple_queue.put(message)
        return HttpResponse('Sent: "%s"' % message)


def consume(request):
    with Connection(settings.RABBITMQ_URL) as conn:
        simple_queue = conn.SimpleQueue('simple_queue')
        message = simple_queue.get(block=True, timeout=1)
        message.ack()
        simple_queue.close()
        return HttpResponse('Received: "%s"' % message.payload)
