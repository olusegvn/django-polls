# Generated by Django 3.2.10 on 2021-12-24 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='was_published_recenetly',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
