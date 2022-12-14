# Generated by Django 3.2.15 on 2022-08-27 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField()),
                ('min_people', models.IntegerField()),
                ('max_people', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot', models.DateField()),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantbooking.customer')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantbooking.table')),
            ],
        ),
    ]
