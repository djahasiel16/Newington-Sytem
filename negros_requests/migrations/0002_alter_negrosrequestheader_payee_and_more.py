# Generated by Django 5.0 on 2024-02-15 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negros_requests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negrosrequestheader',
            name='payee',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='negrosrequestitems',
            name='description',
            field=models.CharField(max_length=60),
        ),
    ]
