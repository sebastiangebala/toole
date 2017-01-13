# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toole', '0004_kariera'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kariera',
            old_name='image',
            new_name='plik',
        ),
    ]
