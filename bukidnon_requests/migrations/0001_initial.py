# Generated by Django 5.0 on 2024-02-19 01:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=53)),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BukidnonRequestHeader',
            fields=[
                ('rs_number', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('particulars', models.CharField(max_length=100)),
                ('payee', models.CharField(blank=True, max_length=70, null=True)),
                ('project', models.CharField(max_length=150)),
                ('urgent', models.BooleanField()),
                ('note', models.CharField(blank=True, max_length=165, null=True)),
                ('date_requested', models.DateField()),
                ('date_needed', models.DateField()),
                ('last_modified', models.DateField(auto_now_add=True)),
                ('created', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AuthorizedPersons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=53)),
                ('title', models.CharField(max_length=30)),
                ('signature', models.ImageField(blank=True, upload_to='signatures/')),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bukidnon_requests.bukidnonrequestheader')),
            ],
        ),
        migrations.CreateModel(
            name='BukidnonRequestItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(blank=True, max_length=100)),
                ('ignore', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=60)),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('unit', models.CharField(blank=True, max_length=20)),
                ('unit_cost', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('served', models.BooleanField(default=False)),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bukidnon_requests.bukidnonrequestheader')),
            ],
        ),
        migrations.CreateModel(
            name='Monitoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PO_no', models.CharField(blank=True, max_length=100, null=True)),
                ('PO_date', models.DateField(blank=True, null=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('receiving_report', models.CharField(blank=True, max_length=100, null=True)),
                ('DR_no', models.CharField(blank=True, max_length=16, null=True)),
                ('SI_no', models.CharField(blank=True, max_length=16, null=True)),
                ('OR_no', models.CharField(blank=True, max_length=16, null=True)),
                ('CR_no', models.CharField(blank=True, max_length=16, null=True)),
                ('withdrawal_no', models.CharField(blank=True, max_length=16, null=True)),
                ('item_date', models.DateField(blank=True, null=True)),
                ('header', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bukidnon_requests.bukidnonrequestitems')),
            ],
        ),
    ]
