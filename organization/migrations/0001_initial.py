# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('identifier', models.CharField(max_length=255)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('postalCode', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('phoneNum', models.CharField(max_length=255)),
                ('faxNum', models.CharField(max_length=255)),
                ('ttyNum', models.CharField(max_length=255)),
                ('orgEmail', models.CharField(max_length=255)),
                ('orgUrl', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
