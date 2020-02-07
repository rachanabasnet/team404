# Generated by Django 2.2 on 2020-02-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=255)),
                ('e_location', models.CharField(max_length=255)),
                ('e_image', models.ImageField(blank=True, null=True, upload_to='EventImg')),
                ('e_description', models.TextField(max_length=1500)),
                ('e_duration', models.CharField(max_length=255)),
                ('e_theme', models.CharField(choices=[('adventure', 'adventure'), ('nature', 'nature'), ('culture', 'culture'), ('food', 'food'), ('entertainment', 'entertainment'), ('leisure', 'leisure')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='HotelModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_name', models.CharField(max_length=255)),
                ('h_location', models.CharField(max_length=255)),
                ('h_description', models.TextField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.CharField(max_length=255)),
                ('r_location', models.CharField(max_length=255)),
                ('r_description', models.TextField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='TouristModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=255)),
                ('t_location', models.CharField(max_length=255)),
            ],
        ),
    ]