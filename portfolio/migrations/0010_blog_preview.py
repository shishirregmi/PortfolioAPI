# Generated by Django 4.2.2 on 2023-06-21 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_about_about_alter_about_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='preview',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
