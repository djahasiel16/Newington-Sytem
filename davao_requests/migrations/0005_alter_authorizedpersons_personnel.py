# Generated by Django 5.0 on 2024-02-28 03:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('davao_requests', '0004_alter_authorizedpersons_name_and_more'),
        ('main', '0005_remove_personnel_personnel_name_title_uniq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizedpersons',
            name='personnel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authorized_persons', to='main.personnel'),
        ),
    ]
