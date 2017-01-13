# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('toole', '0009_auto_20170113_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kariera',
            name='plik',
            field=models.FileField(upload_to='', default=datetime.datetime(2017, 1, 13, 21, 58, 1, 23989, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
