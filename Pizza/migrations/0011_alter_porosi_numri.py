# Generated by Django 5.2.1 on 2025-05-29 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pizza', '0010_remove_porosi_email_porosi_numri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porosi',
            name='numri',
            field=models.CharField(max_length=15),
        ),
    ]
