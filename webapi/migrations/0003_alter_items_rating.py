# Generated by Django 4.1.2 on 2022-10-18 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0002_items_delete_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Rating',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]