# Generated by Django 5.0 on 2024-02-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('davao_requests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='davaorequestitems',
            name='ignore',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='davaorequestheader',
            name='date_needed',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='davaorequestitems',
            name='amount',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='davaorequestitems',
            name='unit_cost',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]