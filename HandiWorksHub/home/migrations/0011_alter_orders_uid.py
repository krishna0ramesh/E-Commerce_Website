# Generated by Django 4.2.1 on 2023-08-31 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='uid',
            field=models.CharField(max_length=20),
        ),
    ]
