# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toole', '0008_auto_20170112_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kariera',
            name='plik',
            field=models.FileField(null=True, upload_to='', blank=True),
        ),
    ]
