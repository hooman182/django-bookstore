# Generated by Django 5.1 on 2024-08-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(),
        ),
    ]
