# Generated by Django 4.0.5 on 2022-06-04 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='slug',
            field=models.SlugField(auto_created=True, default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='slug',
            field=models.SlugField(auto_created=True, default=1, max_length=150),
            preserve_default=False,
        ),
    ]