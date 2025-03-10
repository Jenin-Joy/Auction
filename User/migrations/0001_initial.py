# Generated by Django 5.1.6 on 2025-03-01 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Artist', '0001_initial'),
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_auctionbody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auctionbody_amount', models.CharField(max_length=30)),
                ('auctionbody_status', models.IntegerField(default=0)),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artist.tbl_auctionhead')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_timmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timmer', models.TimeField()),
                ('timmer_status', models.IntegerField(default=0)),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artist.tbl_auctionhead')),
            ],
        ),
    ]
