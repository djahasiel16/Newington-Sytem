# Generated by Django 5.0 on 2024-02-29 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_personnel_personnel_name_title_uniq'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]
