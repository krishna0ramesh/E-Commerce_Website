# Generated by Django 4.2.1 on 2023-08-30 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_planters'),
    ]

    operations = [
        migrations.CreateModel(
            name='candles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candle_name', models.CharField(max_length=20)),
                ('candle_id', models.IntegerField(null=True)),
                ('candle_img', models.ImageField(null=True, upload_to='products')),
            ],
        ),
        migrations.AddField(
            model_name='planters',
            name='planter_img',
            field=models.ImageField(null=True, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='ceramics',
            name='ceramic_img',
            field=models.ImageField(null=True, upload_to='products'),
        ),
    ]
