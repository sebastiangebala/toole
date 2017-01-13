# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('toole', '0006_auto_20170112_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='kariera',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 12, 17, 52, 7, 366938, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
