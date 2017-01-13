# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('toole', '0005_auto_20170112_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kariera',
            name='plik',
            field=models.FileField(default=datetime.datetime(2017, 1, 12, 17, 51, 25, 609553, tzinfo=utc), upload_to='documents/'),
            preserve_default=False,
        ),
    ]
