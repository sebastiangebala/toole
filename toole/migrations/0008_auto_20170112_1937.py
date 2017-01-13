# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toole', '0007_kariera_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kariera',
            name='plik',
            field=models.FileField(upload_to=''),
        ),
    ]
