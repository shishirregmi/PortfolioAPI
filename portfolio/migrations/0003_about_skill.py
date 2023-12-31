# Generated by Django 4.2.2 on 2023-06-21 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_social'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilepic', models.ImageField(upload_to='about/')),
                ('Title', models.CharField(max_length=255)),
                ('Description', models.TextField()),
                ('BirthDate', models.DateField()),
                ('Education', models.CharField(max_length=255)),
                ('email1', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('About', models.TextField()),
                ('Resume', models.FileField(upload_to='about/')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('level', models.IntegerField()),
            ],
            options={
                'ordering': ['-level'],
            },
        ),
    ]
