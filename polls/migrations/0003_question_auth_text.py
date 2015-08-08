# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150724_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='auth_text',
            field=models.CharField(default='bob', max_length=200),
            preserve_default=False,
        ),
    ]
