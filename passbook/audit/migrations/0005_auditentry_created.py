# Generated by Django 2.1.4 on 2018-12-11 15:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passbook_audit', '0004_auto_20181210_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditentry',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
