# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toole', '0003_auto_20170103_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kariera',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('stanowisko', models.CharField(max_length=200)),
                ('image', models.FileField(blank=True, upload_to='', null=True)),
            ],
        ),
    ]
