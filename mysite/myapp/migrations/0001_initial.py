# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhraseOfTheDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phrase', models.TextField()),
            ],
            options={
                'db_table': b'phrase_of_the_day',
            },
            bases=(models.Model,),
        ),
        migrations.RunSQL('''
INSERT INTO phrase_of_the_day(phrase) VALUES
    ('¡Qué extraño!')
        ''')
    ]
