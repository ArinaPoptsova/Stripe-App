# Generated by Django 4.1.7 on 2023-02-17 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_item_currency'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('name', 'currency')},
        ),
    ]
