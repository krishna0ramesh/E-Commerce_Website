# Generated by Django 4.2.1 on 2023-08-31 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_orders_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='customize',
            field=models.TextField(null=True),
        ),
    ]