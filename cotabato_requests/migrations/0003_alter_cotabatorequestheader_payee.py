# Generated by Django 5.0 on 2024-02-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotabato_requests', '0002_alter_cotabatorequestheader_payee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotabatorequestheader',
            name='payee',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]