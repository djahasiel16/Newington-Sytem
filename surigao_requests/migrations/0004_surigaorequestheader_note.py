# Generated by Django 5.0 on 2024-02-16 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surigao_requests', '0003_alter_surigaorequestheader_payee'),
    ]

    operations = [
        migrations.AddField(
            model_name='surigaorequestheader',
            name='note',
            field=models.CharField(blank=True, max_length=165, null=True),
        ),
    ]
