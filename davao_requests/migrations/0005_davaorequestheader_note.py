# Generated by Django 5.0 on 2024-02-16 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('davao_requests', '0004_alter_davaorequestheader_payee'),
    ]

    operations = [
        migrations.AddField(
            model_name='davaorequestheader',
            name='note',
            field=models.CharField(blank=True, max_length=165, null=True),
        ),
    ]