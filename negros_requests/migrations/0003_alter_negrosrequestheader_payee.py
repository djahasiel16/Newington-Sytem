# Generated by Django 5.0 on 2024-02-15 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negros_requests', '0002_alter_negrosrequestheader_payee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negrosrequestheader',
            name='payee',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
