# Generated by Django 5.0.7 on 2024-07-13 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0002_promotion_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
