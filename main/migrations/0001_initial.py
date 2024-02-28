# Generated by Django 5.0 on 2024-02-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CotabatoAuthorizedPersons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=60)),
                ('middle_initial', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60)),
                ('role', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='DavaoAuthorizedPersons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=60)),
                ('middle_initial', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60)),
                ('role', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='NegrosAuthorizedPersons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=60)),
                ('middle_initial', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60)),
                ('role', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=53)),
                ('title', models.CharField(max_length=30)),
                ('signature', models.ImageField(blank=True, upload_to='signatures/')),
            ],
        ),
        migrations.CreateModel(
            name='SurigaoAuthorizedPersons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=60)),
                ('middle_initial', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60)),
                ('role', models.CharField(max_length=60)),
            ],
        ),
    ]