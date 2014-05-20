from django.db import models


class PhraseOfTheDay(models.Model):
    phrase = models.TextField()

    class Meta:
        db_table = 'phrase_of_the_day'
