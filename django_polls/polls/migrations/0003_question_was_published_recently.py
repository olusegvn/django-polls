# Generated by Django 3.2.10 on 2021-12-24 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20211224_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='was_published_recently',
            field=models.BooleanField(default=False),
        ),
    ]
