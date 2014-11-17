# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title_text', models.CharField(max_length=500)),
                ('principal', models.FloatField(default=1000000)),
                ('number_of_months', models.IntegerField(default=12)),
                ('annual_interest_rate', models.FloatField(default=0.03)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
