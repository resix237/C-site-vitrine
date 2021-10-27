# Generated by Django 3.2 on 2021-10-11 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carossel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200, verbose_name='nom')),
                ('frst_image', models.ImageField(upload_to='main/images/carossels')),
                ('scd_image', models.ImageField(upload_to='main/images/carossels')),
                ('trd_image', models.ImageField(upload_to='main/images/carossels')),
                ('title_1', models.CharField(max_length=200, verbose_name='titre1')),
                ('title_2', models.CharField(max_length=200, verbose_name='titre2')),
                ('title_3', models.CharField(max_length=200, verbose_name='titre3')),
                ('descrpt_1', models.TextField(blank=True, verbose_name='dscrpt1')),
                ('descrpt_2', models.TextField(blank=True, verbose_name='dscrpt2')),
                ('descrpt_3', models.TextField(blank=True, verbose_name='dscrpt3')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200, verbose_name='Nom')),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='home_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('about_image', models.ImageField(upload_to='main/images')),
                ('about_description', models.TextField(blank=True, verbose_name='aboutDescription')),
                ('about_banniere', models.TextField(blank=True, verbose_name='banniere')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('senderName', models.CharField(max_length=200, verbose_name='Nom complet')),
                ('senderEmail', models.EmailField(max_length=254, verbose_name='votre email')),
                ('mainMessage', models.TextField(blank=True, verbose_name='Ton message')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200, verbose_name='Nom')),
                ('descriptionBref', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='main/images/services')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('subEmail', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
