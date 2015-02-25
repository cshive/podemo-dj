# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20150209_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='address1',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='address2',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='city',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='country',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='faxNum',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='orgEmail',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='orgStatus',
            field=models.ForeignKey(blank=True, null=True, to='organization.OrgStatus'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='orgType',
            field=models.ForeignKey(blank=True, null=True, to='organization.OrgType'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='orgUrl',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='phoneNum',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='postalCode',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='state',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='ttyNum',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
    ]
