# Generated by Django 2.2.4 on 2019-09-06 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='img',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
    ]