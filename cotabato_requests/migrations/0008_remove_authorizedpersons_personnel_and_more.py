# Generated by Django 5.0 on 2024-02-28 05:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotabato_requests', '0007_authorizedpersons_personnel_authorizedpersons_signed_and_more'),
        ('main', '0005_remove_personnel_personnel_name_title_uniq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorizedpersons',
            name='personnel',
        ),
        migrations.AddField(
            model_name='authorizedpersons',
            name='personnel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='AuthorizedPersonsCotabato', to='main.personnel'),
            preserve_default=False,
        ),
    ]
