# Generated by Django 4.1.1 on 2022-10-14 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
