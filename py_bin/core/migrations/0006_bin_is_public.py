# Generated by Django 2.2 on 2019-04-10 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190408_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='bin',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
