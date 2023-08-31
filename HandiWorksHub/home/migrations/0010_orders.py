# Generated by Django 4.2.1 on 2023-08-31 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_candles_candle_id_alter_cards_card_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.CharField(max_length=20)),
                ('phno', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('uid', models.CharField(max_length=10)),
                ('num', models.IntegerField()),
                ('bookedOn', models.DateField(auto_now=True)),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.items')),
            ],
        ),
    ]