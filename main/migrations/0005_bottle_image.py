# Generated by Django 5.2.1 on 2025-05-08 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_bottle_liquid_density'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='bottle_images/'),
        ),
    ]
