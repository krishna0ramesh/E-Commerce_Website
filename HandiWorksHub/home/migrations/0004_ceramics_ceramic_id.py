# Generated by Django 4.2.1 on 2023-08-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_ceramic_ceramics'),
    ]

    operations = [
        migrations.AddField(
            model_name='ceramics',
            name='ceramic_id',
            field=models.IntegerField(null=True),
        ),
    ]
