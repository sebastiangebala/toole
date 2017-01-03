# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toole', '0002_partner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partner',
            old_name='text',
            new_name='link',
        ),
    ]
