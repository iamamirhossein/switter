# Generated by Django 4.0.1 on 2022-02-09 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switter', '0002_fave'),
    ]

    operations = [
        migrations.AddField(
            model_name='sweet',
            name='re_sweet',
            field=models.BooleanField(default=True),
        ),
    ]
